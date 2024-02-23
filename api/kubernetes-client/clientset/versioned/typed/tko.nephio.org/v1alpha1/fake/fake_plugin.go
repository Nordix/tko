// Code generated by client-gen. DO NOT EDIT.

package fake

import (
	"context"

	v1alpha1 "github.com/nephio-experimental/tko/api/krm/tko.nephio.org/v1alpha1"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	labels "k8s.io/apimachinery/pkg/labels"
	types "k8s.io/apimachinery/pkg/types"
	watch "k8s.io/apimachinery/pkg/watch"
	testing "k8s.io/client-go/testing"
)

// FakePlugins implements PluginInterface
type FakePlugins struct {
	Fake *FakeTkoV1alpha1
	ns   string
}

var pluginsResource = v1alpha1.SchemeGroupVersion.WithResource("plugins")

var pluginsKind = v1alpha1.SchemeGroupVersion.WithKind("Plugin")

// Get takes name of the plugin, and returns the corresponding plugin object, and an error if there is any.
func (c *FakePlugins) Get(ctx context.Context, name string, options v1.GetOptions) (result *v1alpha1.Plugin, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewGetAction(pluginsResource, c.ns, name), &v1alpha1.Plugin{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.Plugin), err
}

// List takes label and field selectors, and returns the list of Plugins that match those selectors.
func (c *FakePlugins) List(ctx context.Context, opts v1.ListOptions) (result *v1alpha1.PluginList, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewListAction(pluginsResource, pluginsKind, c.ns, opts), &v1alpha1.PluginList{})

	if obj == nil {
		return nil, err
	}

	label, _, _ := testing.ExtractFromListOptions(opts)
	if label == nil {
		label = labels.Everything()
	}
	list := &v1alpha1.PluginList{ListMeta: obj.(*v1alpha1.PluginList).ListMeta}
	for _, item := range obj.(*v1alpha1.PluginList).Items {
		if label.Matches(labels.Set(item.Labels)) {
			list.Items = append(list.Items, item)
		}
	}
	return list, err
}

// Watch returns a watch.Interface that watches the requested plugins.
func (c *FakePlugins) Watch(ctx context.Context, opts v1.ListOptions) (watch.Interface, error) {
	return c.Fake.
		InvokesWatch(testing.NewWatchAction(pluginsResource, c.ns, opts))

}

// Create takes the representation of a plugin and creates it.  Returns the server's representation of the plugin, and an error, if there is any.
func (c *FakePlugins) Create(ctx context.Context, plugin *v1alpha1.Plugin, opts v1.CreateOptions) (result *v1alpha1.Plugin, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewCreateAction(pluginsResource, c.ns, plugin), &v1alpha1.Plugin{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.Plugin), err
}

// Update takes the representation of a plugin and updates it. Returns the server's representation of the plugin, and an error, if there is any.
func (c *FakePlugins) Update(ctx context.Context, plugin *v1alpha1.Plugin, opts v1.UpdateOptions) (result *v1alpha1.Plugin, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewUpdateAction(pluginsResource, c.ns, plugin), &v1alpha1.Plugin{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.Plugin), err
}

// UpdateStatus was generated because the type contains a Status member.
// Add a +genclient:noStatus comment above the type to avoid generating UpdateStatus().
func (c *FakePlugins) UpdateStatus(ctx context.Context, plugin *v1alpha1.Plugin, opts v1.UpdateOptions) (*v1alpha1.Plugin, error) {
	obj, err := c.Fake.
		Invokes(testing.NewUpdateSubresourceAction(pluginsResource, "status", c.ns, plugin), &v1alpha1.Plugin{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.Plugin), err
}

// Delete takes name of the plugin and deletes it. Returns an error if one occurs.
func (c *FakePlugins) Delete(ctx context.Context, name string, opts v1.DeleteOptions) error {
	_, err := c.Fake.
		Invokes(testing.NewDeleteActionWithOptions(pluginsResource, c.ns, name, opts), &v1alpha1.Plugin{})

	return err
}

// DeleteCollection deletes a collection of objects.
func (c *FakePlugins) DeleteCollection(ctx context.Context, opts v1.DeleteOptions, listOpts v1.ListOptions) error {
	action := testing.NewDeleteCollectionAction(pluginsResource, c.ns, listOpts)

	_, err := c.Fake.Invokes(action, &v1alpha1.PluginList{})
	return err
}

// Patch applies the patch and returns the patched plugin.
func (c *FakePlugins) Patch(ctx context.Context, name string, pt types.PatchType, data []byte, opts v1.PatchOptions, subresources ...string) (result *v1alpha1.Plugin, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewPatchSubresourceAction(pluginsResource, c.ns, name, pt, data, subresources...), &v1alpha1.Plugin{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1alpha1.Plugin), err
}
