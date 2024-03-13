package memory

import (
	contextpkg "context"

	"github.com/nephio-experimental/tko/backend"
	"github.com/tliron/kutil/util"
)

// ([backend.Backend] interface)
func (self *MemoryBackend) SetPlugin(context contextpkg.Context, plugin *backend.Plugin) error {
	self.lock.Lock()
	defer self.lock.Unlock()

	self.plugins[plugin.PluginID] = plugin

	return nil
}

// ([backend.Backend] interface)
func (self *MemoryBackend) GetPlugin(context contextpkg.Context, pluginId backend.PluginID) (*backend.Plugin, error) {
	self.lock.Lock()
	defer self.lock.Unlock()

	if plugin, ok := self.plugins[pluginId]; ok {
		return plugin.Clone(), nil
	} else {
		return nil, backend.NewNotFoundErrorf("plugin: %s", pluginId)
	}
}

// ([backend.Backend] interface)
func (self *MemoryBackend) DeletePlugin(context contextpkg.Context, pluginId backend.PluginID) error {
	self.lock.Lock()
	defer self.lock.Unlock()

	if _, ok := self.plugins[pluginId]; ok {
		delete(self.plugins, pluginId)
		return nil
	} else {
		return backend.NewNotFoundErrorf("plugin: %s", pluginId)
	}
}

// ([backend.Backend] interface)
func (self *MemoryBackend) ListPlugins(context contextpkg.Context, selectPlugins backend.SelectPlugins, window backend.Window) (util.Results[backend.Plugin], error) {
	self.lock.Lock()

	var plugins []backend.Plugin
	for _, plugin := range self.plugins {
		if (selectPlugins.Type != nil) && (*selectPlugins.Type != "") {
			if *selectPlugins.Type != plugin.Type {
				continue
			}
		}

		if (selectPlugins.Executor != nil) && (*selectPlugins.Executor != "") {
			if *selectPlugins.Executor != plugin.Executor {
				continue
			}
		}

		if !backend.IDMatchesPatterns(plugin.Name, selectPlugins.NamePatterns) {
			continue
		}

		if selectPlugins.Trigger != nil {
			var found bool
			for _, trigger := range plugin.Triggers {
				if selectPlugins.Trigger.Equals(trigger) {
					found = true
					break
				}
			}
			if !found {
				continue
			}
		}

		plugins = append(plugins, *plugin)
	}

	self.lock.Unlock()

	backend.SortPlugins(plugins)

	length := uint(len(plugins))
	if window.Offset > length {
		plugins = nil
	} else if end := window.Offset + window.MaxCount; end > length {
		plugins = plugins[window.Offset:]
	} else {
		plugins = plugins[window.Offset:end]
	}

	return util.NewResultsSlice(plugins), nil
}

// ([backend.Backend] interface)
func (self *MemoryBackend) PurgePlugins(context contextpkg.Context, selectPlugins backend.SelectPlugins) error {
	return backend.NewNotImplementedError("PurgePlugins")
}
