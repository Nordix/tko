package backend

import (
	"slices"
	"strings"
	"time"

	"github.com/nephio-experimental/tko/util"
)

//
// SiteInfo
//

type SiteInfo struct {
	SiteID        string
	TemplateID    string
	Metadata      map[string]string
	Updated       time.Time // millisecond precision
	DeploymentIDs []string
}

func (self *SiteInfo) Clone(withDeployments bool) SiteInfo {
	if withDeployments {
		return SiteInfo{
			SiteID:        self.SiteID,
			TemplateID:    self.TemplateID,
			Metadata:      util.CloneStringMap(self.Metadata),
			Updated:       self.Updated,
			DeploymentIDs: util.CloneStringSet(self.DeploymentIDs),
		}
	} else {
		return SiteInfo{
			SiteID:     self.SiteID,
			TemplateID: self.TemplateID,
			Metadata:   util.CloneStringMap(self.Metadata),
			Updated:    self.Updated,
		}
	}
}

func (self *SiteInfo) UpdateFromResources(resources util.Resources) {
	updateMetadataFromResources(self.Metadata, resources)
}

func (self *SiteInfo) MergeTemplateInfo(templateInfo *TemplateInfo) {
	metadata := make(map[string]string)

	for key, value := range templateInfo.Metadata {
		metadata[key] = value
	}

	for key, value := range self.Metadata {
		metadata[key] = value
	}

	self.Metadata = metadata
}

func SortSiteInfos(siteInfos []SiteInfo) {
	slices.SortFunc(siteInfos, func(a SiteInfo, b SiteInfo) int {
		return strings.Compare(a.SiteID, b.SiteID)
	})
}

//
// Site
//

type Site struct {
	SiteInfo
	Resources util.Resources
}

func NewSiteFromBytes(siteId string, templateId string, metadata map[string]string, resourcesFormat string, resources []byte) (*Site, error) {
	if resources, err := util.DecodeResources(resourcesFormat, resources); err == nil {
		if metadata == nil {
			metadata = make(map[string]string)
		}
		return &Site{
			SiteInfo: SiteInfo{
				SiteID:     siteId,
				TemplateID: templateId,
				Metadata:   metadata,
			},
			Resources: resources,
		}, nil
	} else {
		return nil, err
	}
}

func (self *Site) Clone(withDeployments bool) *Site {
	return &Site{
		SiteInfo:  self.SiteInfo.Clone(withDeployments),
		Resources: util.CloneResources(self.Resources),
	}
}

func (self *Site) UpdateFromResources() {
	self.SiteInfo.UpdateFromResources(self.Resources)
}

func (self *Site) EncodeResources(format string) ([]byte, error) {
	return util.EncodeResources(format, self.Resources)
}

func (self *Site) AddDeployment(deploymentId string) bool {
	var ok bool
	self.DeploymentIDs, ok = util.AddToStringSet(self.DeploymentIDs, deploymentId)
	return ok
}

func (self *Site) RemoveDeployment(deploymentId string) bool {
	var ok bool
	self.DeploymentIDs, ok = util.RemoveFromStringSet(self.DeploymentIDs, deploymentId)
	return ok
}

func (self *Site) MergeTemplate(template *Template) {
	self.MergeTemplateInfo(&template.TemplateInfo)

	resources := util.CloneResources(template.Resources)
	resources = util.MergeResources(resources, self.Resources...)

	self.Resources = resources
}
