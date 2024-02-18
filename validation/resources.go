package validation

import (
	contextpkg "context"
	"errors"
	"fmt"
	"sync"

	"github.com/nephio-experimental/tko/util"
)

func (self *Validation) ValidateResources(resources util.Resources, complete bool) error {
	self.validators = sync.Map{}

	var errs []error

	for _, resource := range resources {
		if resourceIdentifier, ok := util.NewResourceIdentifierForResource(resource); ok {
			if validators, err := self.GetValidators(resourceIdentifier.GVK, complete); err == nil {
				if len(validators) > 0 {
					validationContext := self.NewContext(resources, resourceIdentifier, complete)

					for _, validate := range validators {
						context, cancel := contextpkg.WithTimeout(contextpkg.Background(), self.Timeout)
						errs = append(errs, wrapErrors(resourceIdentifier, validate(context, validationContext))...)
						cancel()
					}
				}
			} else {
				errs = append(errs, err)
			}
		} else {
			errs = append(errs, wrapErrors(resourceIdentifier, self.Kubeconform(resource, complete))...)
		}
	}

	return errors.Join(errs...)
}

// ([ValidatorFunc] signature)
func (self *Validation) DefaultValidate(context contextpkg.Context, validationContext *Context) []error {
	if resource, ok := validationContext.GetResource(); ok {
		return self.Kubeconform(resource, validationContext.Complete)
	} else {
		return nil
	}
}

// Utils

func wrapErrors(resourceIdentifier util.ResourceIdentifier, errors []error) []error {
	wrappedErrors := make([]error, len(errors))
	for index, err := range errors {
		wrappedErrors[index] = fmt.Errorf("%s: %w", resourceIdentifier, err)
	}
	return wrappedErrors
}
