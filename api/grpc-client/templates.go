package client

import (
	contextpkg "context"
	"strings"
	"time"

	api "github.com/nephio-experimental/tko/api/grpc"
	tkoutil "github.com/nephio-experimental/tko/util"
	"github.com/tliron/kutil/util"
)

type TemplateInfo struct {
	TemplateID    string            `json:"templateId" yaml:"templateId"`
	Metadata      map[string]string `json:"metadata,omitempty" yaml:"metadata,omitempty"`
	Updated       time.Time         `json:"updated" yaml:"updated"`
	DeploymentIDs []string          `json:"deploymentIds,omitempty" yaml:"deploymentIds,omitempty"`
}

type Template struct {
	TemplateInfo
	Package tkoutil.Package `json:"package" yaml:"package"`
}

func (self *Client) RegisterTemplate(templateId string, metadata map[string]string, package_ tkoutil.Package) (bool, string, error) {
	if package__, err := self.encodePackage(package_); err == nil {
		return self.RegisterTemplateRaw(templateId, metadata, self.PackageFormat, package__)
	} else {
		return false, "", err
	}
}

func (self *Client) RegisterTemplateRaw(templateId string, metadata map[string]string, packageFormat string, package_ []byte) (bool, string, error) {
	if apiClient, err := self.APIClient(); err == nil {
		context, cancel := contextpkg.WithTimeout(contextpkg.Background(), self.Timeout)
		defer cancel()

		self.log.Info("registerTemplate",
			"templateId", templateId,
			"metadata", metadata,
			"packageFormat", packageFormat)
		if response, err := apiClient.RegisterTemplate(context, &api.Template{
			TemplateId:    templateId,
			Metadata:      metadata,
			PackageFormat: packageFormat,
			Package:       package_,
		}); err == nil {
			return response.Registered, response.NotRegisteredReason, nil
		} else {
			return false, "", err
		}
	} else {
		return false, "", err
	}
}

func (self *Client) GetTemplate(templateId string) (Template, bool, error) {
	if apiClient, err := self.APIClient(); err == nil {
		context, cancel := contextpkg.WithTimeout(contextpkg.Background(), self.Timeout)
		defer cancel()

		self.log.Info("getTemplate",
			"templateId", templateId)
		if template, err := apiClient.GetTemplate(context, &api.GetTemplate{TemplateId: templateId, PreferredPackageFormat: self.PackageFormat}); err == nil {
			if package_, err := tkoutil.DecodePackage(template.PackageFormat, template.Package); err == nil {
				return Template{
					TemplateInfo: TemplateInfo{
						TemplateID:    template.TemplateId,
						Metadata:      template.Metadata,
						Updated:       self.toTime(template.Updated),
						DeploymentIDs: template.DeploymentIds,
					},
					Package: package_,
				}, true, nil
			} else {
				return Template{}, false, err
			}
		} else if IsNotFoundError(err) {
			return Template{}, false, nil
		} else {
			return Template{}, false, err
		}
	} else {
		return Template{}, false, err
	}
}

func (self *Client) DeleteTemplate(templateId string) (bool, string, error) {
	if apiClient, err := self.APIClient(); err == nil {
		context, cancel := contextpkg.WithTimeout(contextpkg.Background(), self.Timeout)
		defer cancel()

		self.log.Info("deleteTemplate",
			"templateId", templateId)
		if response, err := apiClient.DeleteTemplate(context, &api.TemplateID{TemplateId: templateId}); err == nil {
			return response.Deleted, response.NotDeletedReason, nil
		} else {
			return false, "", err
		}
	} else {
		return false, "", err
	}
}

type ListTemplates struct {
	Offset             uint
	MaxCount           uint
	TemplateIDPatterns []string
	MetadataPatterns   map[string]string
}

// ([fmt.Stringer] interface)
func (self ListTemplates) String() string {
	var s []string
	if len(self.TemplateIDPatterns) > 0 {
		s = append(s, "templateIdPatterns="+strings.Join(self.TemplateIDPatterns, ","))
	}
	if (self.MetadataPatterns != nil) && (len(self.MetadataPatterns) > 0) {
		s = append(s, "metadataPatterns="+stringifyStringMap(self.MetadataPatterns))
	}
	return strings.Join(s, " ")
}

func (self *Client) ListTemplates(listTemplates ListTemplates) (util.Results[TemplateInfo], error) {
	if apiClient, err := self.APIClient(); err == nil {
		context, cancel := contextpkg.WithTimeout(contextpkg.Background(), self.Timeout)

		self.log.Info("listTemplates",
			"listTemplates", listTemplates)
		if client, err := apiClient.ListTemplates(context, &api.ListTemplates{
			Offset:             uint32(listTemplates.Offset),
			MaxCount:           uint32(listTemplates.MaxCount),
			TemplateIdPatterns: listTemplates.TemplateIDPatterns,
			MetadataPatterns:   listTemplates.MetadataPatterns,
		}); err == nil {
			stream := util.NewResultsStream[TemplateInfo](cancel)

			go func() {
				for {
					if listedTemplate, err := client.Recv(); err == nil {
						stream.Send(TemplateInfo{
							TemplateID:    listedTemplate.TemplateId,
							Metadata:      listedTemplate.Metadata,
							Updated:       self.toTime(listedTemplate.Updated),
							DeploymentIDs: listedTemplate.DeploymentIds,
						})
					} else {
						stream.Close(err) // special handling for io.EOF
						return
					}
				}
			}()

			return stream, nil
		} else {
			cancel()
			return nil, err
		}
	} else {
		return nil, err
	}
}
