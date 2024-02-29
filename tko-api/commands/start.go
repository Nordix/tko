package commands

import (
	"context"
	"os"
	"time"

	grpcclient "github.com/nephio-experimental/tko/api/grpc-client"
	grpcserver "github.com/nephio-experimental/tko/api/grpc-server"
	httpserver "github.com/nephio-experimental/tko/api/http-server"
	kubernetesserver "github.com/nephio-experimental/tko/api/kubernetes-server"
	backendpkg "github.com/nephio-experimental/tko/backend"
	"github.com/nephio-experimental/tko/backend/memory"
	"github.com/nephio-experimental/tko/backend/spanner"
	"github.com/nephio-experimental/tko/backend/sql"
	tkoutil "github.com/nephio-experimental/tko/util"
	validationpkg "github.com/nephio-experimental/tko/validation"
	"github.com/spf13/cobra"
	"github.com/tliron/commonlog"
	cobrautil "github.com/tliron/kutil/cobra"
	"github.com/tliron/kutil/util"
)

const maxModificationDuration = 10 // seconds

var backendName string
var backendConnection string
var backendClean bool
var grpcIpStackString string
var grpcIpStack util.IPStack
var grpcAddress string
var grpcPort uint
var grpcFormat string
var grpcTimeout float64
var webTimeout float64
var webIpStackString string
var webIpStack util.IPStack
var webAddress string
var webPort uint
var webTimezone string
var kubernetes bool
var kubernetesPort uint
var validatorTimeout float64

func init() {
	rootCommand.AddCommand(startCommand)

	startCommand.Flags().StringVarP(&backendName, "backend", "b", "memory", "backend implementation")
	startCommand.Flags().StringVar(&backendConnection, "backend-connection", "postgresql://tko:tko@localhost:5432/tko", "backend connection")
	startCommand.Flags().BoolVar(&backendClean, "backend-clean", false, "clean backend data on startup")
	startCommand.Flags().StringVar(&grpcIpStackString, "grpc-ip-stack", "dual", "bind IP stack for gRPC server (\"dual\", \"ipv6\", or \"ipv4\")")
	startCommand.Flags().StringVar(&grpcAddress, "grpc-address", "", "bind address for gRPC server")
	startCommand.Flags().UintVar(&grpcPort, "grpc-port", 50050, "bind HTTP/2 port for gRPC server")
	startCommand.Flags().StringVar(&grpcFormat, "grpc-format", "cbor", "preferred format for encoding resources over gRPC (\"yaml\" or \"cbor\")")
	startCommand.Flags().Float64Var(&grpcTimeout, "grpc-timeout", 5.0, "gRPC timeout in seconds")
	startCommand.Flags().Float64Var(&webTimeout, "web-timeout", 5.0, "web read/write timeout in seconds")
	startCommand.Flags().StringVar(&webIpStackString, "web-ip-stack", "dual", "bind IP stack for web server (\"dual\", \"ipv6\", or \"ipv4\")")
	startCommand.Flags().StringVar(&webAddress, "web-address", "", "bind address for web server")
	startCommand.Flags().UintVar(&webPort, "web-port", 50051, "bind HTTP/2 port for web server")
	startCommand.Flags().StringVar(&webTimezone, "web-timezone", "", "web server timezone, e.g. \"UTC\" (empty string for local)")
	startCommand.Flags().BoolVar(&kubernetes, "kubernetes", false, "start Kubernetes aggregated API server")
	startCommand.Flags().UintVar(&kubernetesPort, "kubernetes-port", 50052, "bind port for Kubernetes aggregated API server")
	startCommand.Flags().Float64Var(&validatorTimeout, "validator-timeout", 30.0, "validator timeout in seconds")

	cobrautil.SetFlagsFromEnvironment("TKO_", startCommand)
}

var startCommand = &cobra.Command{
	Use:   "start",
	Short: "Start the TKO API Server",
	Run: func(cmd *cobra.Command, args []string) {
		grpcIpStack = util.IPStack(grpcIpStackString)
		util.FailOnError(grpcIpStack.Validate("grpc-ip-stack"))

		webIpStack = util.IPStack(webIpStackString)
		util.FailOnError(grpcIpStack.Validate("web-ip-stack"))

		Serve()
	},
}

func Serve() {
	// Backend
	var backend backendpkg.Backend
	switch backendName {
	case "memory":
		log.Notice("creating memory backend")
		backend = memory.NewMemoryBackend(maxModificationDuration, commonlog.GetLogger("backend.memory"))

	case "postgresql":
		log.Noticef("creating postgresql backend: %s", backendConnection)
		sqlBackend := sql.NewSQLBackend("pgx", backendConnection, "cbor", maxModificationDuration, commonlog.GetLogger("backend.sql"))
		sqlBackend.DropTablesFirst = backendClean
		backend = sqlBackend

	case "spanner":
		backend = spanner.NewSpannerBackend("/span/tmp/"+os.Getenv("USER")+":database-tliron-codelab", commonlog.GetLogger("backend.spanner"))

	default:
		util.Failf("unsupported backend: %s", backendName)
	}

	var webTimezone_ *time.Location
	if webTimezone != "" {
		var err error
		webTimezone_, err = time.LoadLocation(webTimezone)
		util.FailOnError(err)
	}

	// Client
	client := grpcclient.NewClient(grpcIpStack, grpcAddress, int(grpcPort), grpcFormat, tkoutil.SecondsToDuration(grpcTimeout), commonlog.GetLogger("client"))

	// Wrap backend with validation
	validation, err := validationpkg.NewValidation(client, tkoutil.SecondsToDuration(validatorTimeout), commonlog.GetLogger("validation"))
	util.FailOnError(err)
	validationTicker := tkoutil.NewTicker(10*time.Second, validation.ResetPluginCache)
	util.OnExit(validationTicker.Stop)
	backend = backendpkg.NewValidatingBackend(backend, validation)

	util.FailOnError(backend.Connect(context.TODO()))
	util.OnExitError(func() error {
		return backend.Release(context.TODO())
	})

	// gRPC
	grpcServer := grpcserver.NewServer(backend, grpcIpStack, grpcAddress, int(grpcPort), grpcFormat, commonlog.GetLogger("grpc"))
	util.FailOnError(grpcServer.Start())
	util.OnExit(grpcServer.Stop)

	// HTTP
	httpServer, err := httpserver.NewServer(backend, tkoutil.SecondsToDuration(webTimeout), webIpStack, webAddress, int(webPort), webTimezone_, commonlog.GetLogger("http"))
	util.FailOnError(err)
	util.FailOnError(httpServer.Start())
	util.OnExit(httpServer.Stop)

	// Kubernetes
	if kubernetes {
		kubernetesServer, err := kubernetesserver.NewServer(backend, int(kubernetesPort), commonlog.GetLogger("kubernetes"))
		util.FailOnError(err)
		kubernetesServer.Start()
		util.OnExit(kubernetesServer.Stop)
	}

	// Block forever
	select {}
}
