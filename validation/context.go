package validation

import (
	"github.com/nephio-experimental/tko/util"
)

//
// Context
//

type Context struct {
	Validation              *Validation
	Resources               []util.Resource
	TargetResourceIdentifer util.ResourceIdentifier
	Complete                bool
}

func (self *Validation) NewContext(resources []util.Resource, targetResourceIdentifer util.ResourceIdentifier, complete bool) *Context {
	return &Context{
		Validation:              self,
		Resources:               resources,
		TargetResourceIdentifer: targetResourceIdentifer,
		Complete:                complete,
	}
}

func (self *Context) GetResource() (util.Resource, bool) {
	return self.TargetResourceIdentifer.GetResource(self.Resources)
}
