# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tko/tko.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rtko/tko.proto\x12\x03tko\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xac\x01\n\rAboutResponse\x12\x14\n\x0cinstanceName\x18\x01 \x01(\t\x12\x1b\n\x13instanceDescription\x18\x02 \x01(\t\x12\x12\n\ntkoVersion\x18\x03 \x01(\t\x12\x0f\n\x07\x62\x61\x63kend\x18\x04 \x01(\t\x12\x0f\n\x07ipStack\x18\x05 \x01(\t\x12\x14\n\x0c\x61\x64\x64ressPorts\x18\x06 \x03(\t\x12\x1c\n\x14\x64\x65\x66\x61ultPackageFormat\x18\x07 \x01(\t\"C\n\x10RegisterResponse\x12\x12\n\nregistered\x18\x01 \x01(\x08\x12\x1b\n\x13notRegisteredReason\x18\x02 \x01(\t\";\n\x0e\x44\x65leteResponse\x12\x0f\n\x07\x64\x65leted\x18\x01 \x01(\x08\x12\x18\n\x10notDeletedReason\x18\x02 \x01(\t\"*\n\x06Window\x12\x0e\n\x06offset\x18\x01 \x01(\r\x12\x10\n\x08maxCount\x18\x02 \x01(\r\" \n\nTemplateID\x12\x12\n\ntemplateId\x18\x01 \x01(\t\"\xea\x01\n\x08Template\x12\x12\n\ntemplateId\x18\x01 \x01(\t\x12-\n\x08metadata\x18\x02 \x03(\x0b\x32\x1b.tko.Template.MetadataEntry\x12+\n\x07updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rpackageFormat\x18\x04 \x01(\t\x12\x0f\n\x07package\x18\x05 \x01(\x0c\x12\x15\n\rdeploymentIds\x18\x06 \x03(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xce\x01\n\x0eListedTemplate\x12\x12\n\ntemplateId\x18\x01 \x01(\t\x12\x33\n\x08metadata\x18\x02 \x03(\x0b\x32!.tko.ListedTemplate.MetadataEntry\x12+\n\x07updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rdeploymentIds\x18\x04 \x03(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"A\n\x0bGetTemplate\x12\x12\n\ntemplateId\x18\x01 \x01(\t\x12\x1e\n\x16preferredPackageFormat\x18\x02 \x01(\t\"\xac\x01\n\x0fSelectTemplates\x12\x1a\n\x12templateIdPatterns\x18\x03 \x03(\t\x12\x44\n\x10metadataPatterns\x18\x04 \x03(\x0b\x32*.tko.SelectTemplates.MetadataPatternsEntry\x1a\x37\n\x15MetadataPatternsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"R\n\rListTemplates\x12\x1b\n\x06window\x18\x01 \x01(\x0b\x32\x0b.tko.Window\x12$\n\x06select\x18\x02 \x01(\x0b\x32\x14.tko.SelectTemplates\"\x18\n\x06SiteID\x12\x0e\n\x06siteId\x18\x01 \x01(\t\"\xf2\x01\n\x04Site\x12\x0e\n\x06siteId\x18\x01 \x01(\t\x12\x12\n\ntemplateId\x18\x02 \x01(\t\x12)\n\x08metadata\x18\x03 \x03(\x0b\x32\x17.tko.Site.MetadataEntry\x12+\n\x07updated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rpackageFormat\x18\x05 \x01(\t\x12\x0f\n\x07package\x18\x06 \x01(\x0c\x12\x15\n\rdeploymentIds\x18\x07 \x03(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd6\x01\n\nListedSite\x12\x0e\n\x06siteId\x18\x01 \x01(\t\x12\x12\n\ntemplateId\x18\x02 \x01(\t\x12/\n\x08metadata\x18\x03 \x03(\x0b\x32\x1d.tko.ListedSite.MetadataEntry\x12+\n\x07updated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rdeploymentIds\x18\x05 \x03(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"9\n\x07GetSite\x12\x0e\n\x06siteId\x18\x01 \x01(\t\x12\x1e\n\x16preferredPackageFormat\x18\x02 \x01(\t\"\xbc\x01\n\x0bSelectSites\x12\x16\n\x0esiteIdPatterns\x18\x03 \x03(\t\x12\x1a\n\x12templateIdPatterns\x18\x04 \x03(\t\x12@\n\x10metadataPatterns\x18\x05 \x03(\x0b\x32&.tko.SelectSites.MetadataPatternsEntry\x1a\x37\n\x15MetadataPatternsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"J\n\tListSites\x12\x1b\n\x06window\x18\x01 \x01(\x0b\x32\x0b.tko.Window\x12 \n\x06select\x18\x02 \x01(\x0b\x32\x10.tko.SelectSites\"$\n\x0c\x44\x65ploymentID\x12\x14\n\x0c\x64\x65ploymentId\x18\x01 \x01(\t\"\xea\x02\n\nDeployment\x12\x14\n\x0c\x64\x65ploymentId\x18\x01 \x01(\t\x12\x1a\n\x12parentDeploymentId\x18\x02 \x01(\t\x12\x12\n\ntemplateId\x18\x03 \x01(\t\x12\x0e\n\x06siteId\x18\x04 \x01(\t\x12/\n\x08metadata\x18\x05 \x03(\x0b\x32\x1d.tko.Deployment.MetadataEntry\x12+\n\x07\x63reated\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08prepared\x18\x08 \x01(\x08\x12\x10\n\x08\x61pproved\x18\t \x01(\x08\x12\x15\n\rpackageFormat\x18\n \x01(\t\x12\x0f\n\x07package\x18\x0b \x01(\x0c\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xce\x02\n\x10ListedDeployment\x12\x14\n\x0c\x64\x65ploymentId\x18\x01 \x01(\t\x12\x1a\n\x12parentDeploymentId\x18\x02 \x01(\t\x12\x12\n\ntemplateId\x18\x03 \x01(\t\x12\x0e\n\x06siteId\x18\x04 \x01(\t\x12\x35\n\x08metadata\x18\x05 \x03(\x0b\x32#.tko.ListedDeployment.MetadataEntry\x12+\n\x07\x63reated\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08prepared\x18\x08 \x01(\x08\x12\x10\n\x08\x61pproved\x18\t \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9f\x02\n\x10\x43reateDeployment\x12\x1a\n\x12parentDeploymentId\x18\x01 \x01(\t\x12\x12\n\ntemplateId\x18\x02 \x01(\t\x12\x0e\n\x06siteId\x18\x03 \x01(\t\x12?\n\rmergeMetadata\x18\x04 \x03(\x0b\x32(.tko.CreateDeployment.MergeMetadataEntry\x12\x10\n\x08prepared\x18\x05 \x01(\x08\x12\x10\n\x08\x61pproved\x18\x06 \x01(\x08\x12\x1a\n\x12mergePackageFormat\x18\x07 \x01(\t\x12\x14\n\x0cmergePackage\x18\x08 \x01(\x0c\x1a\x34\n\x12MergeMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"[\n\x18\x43reateDeploymentResponse\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\x12\x18\n\x10notCreatedReason\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x65ploymentId\x18\x03 \x01(\t\"E\n\rGetDeployment\x12\x14\n\x0c\x64\x65ploymentId\x18\x01 \x01(\t\x12\x1e\n\x16preferredPackageFormat\x18\x02 \x01(\t\"\xee\x04\n\x11SelectDeployments\x12\x1f\n\x12parentDeploymentId\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x46\n\x10metadataPatterns\x18\x04 \x03(\x0b\x32,.tko.SelectDeployments.MetadataPatternsEntry\x12\x1a\n\x12templateIdPatterns\x18\x05 \x03(\t\x12V\n\x18templateMetadataPatterns\x18\x06 \x03(\x0b\x32\x34.tko.SelectDeployments.TemplateMetadataPatternsEntry\x12\x16\n\x0esiteIdPatterns\x18\x07 \x03(\t\x12N\n\x14siteMetadataPatterns\x18\x08 \x03(\x0b\x32\x30.tko.SelectDeployments.SiteMetadataPatternsEntry\x12\x15\n\x08prepared\x18\t \x01(\x08H\x01\x88\x01\x01\x12\x15\n\x08\x61pproved\x18\n \x01(\x08H\x02\x88\x01\x01\x1a\x37\n\x15MetadataPatternsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a?\n\x1dTemplateMetadataPatternsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19SiteMetadataPatternsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x15\n\x13_parentDeploymentIdB\x0b\n\t_preparedB\x0b\n\t_approved\"V\n\x0fListDeployments\x12\x1b\n\x06window\x18\x01 \x01(\x0b\x32\x0b.tko.Window\x12&\n\x06select\x18\x02 \x01(\x0b\x32\x16.tko.SelectDeployments\"S\n\x1bStartDeploymentModification\x12\x14\n\x0c\x64\x65ploymentId\x18\x01 \x01(\t\x12\x1e\n\x16preferredPackageFormat\x18\x02 \x01(\t\"\x93\x01\n#StartDeploymentModificationResponse\x12\x0f\n\x07started\x18\x01 \x01(\x08\x12\x18\n\x10notStartedReason\x18\x02 \x01(\t\x12\x19\n\x11modificationToken\x18\x03 \x01(\t\x12\x15\n\rpackageFormat\x18\x04 \x01(\t\x12\x0f\n\x07package\x18\x05 \x01(\x0c\"^\n\x19\x45ndDeploymentModification\x12\x19\n\x11modificationToken\x18\x01 \x01(\t\x12\x15\n\rpackageFormat\x18\x02 \x01(\t\x12\x0f\n\x07package\x18\x03 \x01(\x0c\"f\n!EndDeploymentModificationResponse\x12\x10\n\x08modified\x18\x01 \x01(\x08\x12\x19\n\x11notModifiedReason\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x65ploymentId\x18\x03 \x01(\t\"9\n\x1c\x43\x61ncelDeploymentModification\x12\x19\n\x11modificationToken\x18\x01 \x01(\t\"U\n$CancelDeploymentModificationResponse\x12\x11\n\tcancelled\x18\x01 \x01(\x08\x12\x1a\n\x12notCancelledReason\x18\x02 \x01(\t\"&\n\x08PluginID\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"3\n\x03GVK\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t\"\xc9\x01\n\x06Plugin\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x65xecutor\x18\x03 \x01(\t\x12\x11\n\targuments\x18\x04 \x03(\t\x12/\n\nproperties\x18\x05 \x03(\x0b\x32\x1b.tko.Plugin.PropertiesEntry\x12\x1a\n\x08triggers\x18\x06 \x03(\x0b\x32\x08.tko.GVK\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x91\x01\n\rSelectPlugins\x12\x11\n\x04type\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x0cnamePatterns\x18\x04 \x03(\t\x12\x15\n\x08\x65xecutor\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x07trigger\x18\x06 \x01(\x0b\x32\x08.tko.GVKH\x02\x88\x01\x01\x42\x07\n\x05_typeB\x0b\n\t_executorB\n\n\x08_trigger\"N\n\x0bListPlugins\x12\x1b\n\x06window\x18\x01 \x01(\x0b\x32\x0b.tko.Window\x12\"\n\x06select\x18\x02 \x01(\x0b\x32\x12.tko.SelectPlugins2\xb9\x0b\n\x03\x41PI\x12\x33\n\x05\x61\x62out\x12\x16.google.protobuf.Empty\x1a\x12.tko.AboutResponse\x12\x38\n\x10registerTemplate\x12\r.tko.Template\x1a\x15.tko.RegisterResponse\x12\x36\n\x0e\x64\x65leteTemplate\x12\x0f.tko.TemplateID\x1a\x13.tko.DeleteResponse\x12.\n\x0bgetTemplate\x12\x10.tko.GetTemplate\x1a\r.tko.Template\x12:\n\rlistTemplates\x12\x12.tko.ListTemplates\x1a\x13.tko.ListedTemplate0\x01\x12;\n\x0epurgeTemplates\x12\x14.tko.SelectTemplates\x1a\x13.tko.DeleteResponse\x12\x30\n\x0cregisterSite\x12\t.tko.Site\x1a\x15.tko.RegisterResponse\x12.\n\ndeleteSite\x12\x0b.tko.SiteID\x1a\x13.tko.DeleteResponse\x12\"\n\x07getSite\x12\x0c.tko.GetSite\x1a\t.tko.Site\x12.\n\tlistSites\x12\x0e.tko.ListSites\x1a\x0f.tko.ListedSite0\x01\x12\x33\n\npurgeSites\x12\x10.tko.SelectSites\x1a\x13.tko.DeleteResponse\x12H\n\x10\x63reateDeployment\x12\x15.tko.CreateDeployment\x1a\x1d.tko.CreateDeploymentResponse\x12:\n\x10\x64\x65leteDeployment\x12\x11.tko.DeploymentID\x1a\x13.tko.DeleteResponse\x12\x34\n\rgetDeployment\x12\x12.tko.GetDeployment\x1a\x0f.tko.Deployment\x12@\n\x0flistDeployments\x12\x14.tko.ListDeployments\x1a\x15.tko.ListedDeployment0\x01\x12?\n\x10purgeDeployments\x12\x16.tko.SelectDeployments\x1a\x13.tko.DeleteResponse\x12i\n\x1bstartDeploymentModification\x12 .tko.StartDeploymentModification\x1a(.tko.StartDeploymentModificationResponse\x12\x63\n\x19\x65ndDeploymentModification\x12\x1e.tko.EndDeploymentModification\x1a&.tko.EndDeploymentModificationResponse\x12l\n\x1c\x63\x61ncelDeploymentModification\x12!.tko.CancelDeploymentModification\x1a).tko.CancelDeploymentModificationResponse\x12\x34\n\x0eregisterPlugin\x12\x0b.tko.Plugin\x1a\x15.tko.RegisterResponse\x12\x32\n\x0c\x64\x65letePlugin\x12\r.tko.PluginID\x1a\x13.tko.DeleteResponse\x12\'\n\tgetPlugin\x12\r.tko.PluginID\x1a\x0b.tko.Plugin\x12.\n\x0blistPlugins\x12\x10.tko.ListPlugins\x1a\x0b.tko.Plugin0\x01\x12\x37\n\x0cpurgePlugins\x12\x12.tko.SelectPlugins\x1a\x13.tko.DeleteResponseB-Z+github.com/nephio-experimental/tko/api/grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tko.tko_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/nephio-experimental/tko/api/grpc'
  _globals['_TEMPLATE_METADATAENTRY']._options = None
  _globals['_TEMPLATE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_LISTEDTEMPLATE_METADATAENTRY']._options = None
  _globals['_LISTEDTEMPLATE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SELECTTEMPLATES_METADATAPATTERNSENTRY']._options = None
  _globals['_SELECTTEMPLATES_METADATAPATTERNSENTRY']._serialized_options = b'8\001'
  _globals['_SITE_METADATAENTRY']._options = None
  _globals['_SITE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_LISTEDSITE_METADATAENTRY']._options = None
  _globals['_LISTEDSITE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SELECTSITES_METADATAPATTERNSENTRY']._options = None
  _globals['_SELECTSITES_METADATAPATTERNSENTRY']._serialized_options = b'8\001'
  _globals['_DEPLOYMENT_METADATAENTRY']._options = None
  _globals['_DEPLOYMENT_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_LISTEDDEPLOYMENT_METADATAENTRY']._options = None
  _globals['_LISTEDDEPLOYMENT_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_CREATEDEPLOYMENT_MERGEMETADATAENTRY']._options = None
  _globals['_CREATEDEPLOYMENT_MERGEMETADATAENTRY']._serialized_options = b'8\001'
  _globals['_SELECTDEPLOYMENTS_METADATAPATTERNSENTRY']._options = None
  _globals['_SELECTDEPLOYMENTS_METADATAPATTERNSENTRY']._serialized_options = b'8\001'
  _globals['_SELECTDEPLOYMENTS_TEMPLATEMETADATAPATTERNSENTRY']._options = None
  _globals['_SELECTDEPLOYMENTS_TEMPLATEMETADATAPATTERNSENTRY']._serialized_options = b'8\001'
  _globals['_SELECTDEPLOYMENTS_SITEMETADATAPATTERNSENTRY']._options = None
  _globals['_SELECTDEPLOYMENTS_SITEMETADATAPATTERNSENTRY']._serialized_options = b'8\001'
  _globals['_PLUGIN_PROPERTIESENTRY']._options = None
  _globals['_PLUGIN_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_ABOUTRESPONSE']._serialized_start=85
  _globals['_ABOUTRESPONSE']._serialized_end=257
  _globals['_REGISTERRESPONSE']._serialized_start=259
  _globals['_REGISTERRESPONSE']._serialized_end=326
  _globals['_DELETERESPONSE']._serialized_start=328
  _globals['_DELETERESPONSE']._serialized_end=387
  _globals['_WINDOW']._serialized_start=389
  _globals['_WINDOW']._serialized_end=431
  _globals['_TEMPLATEID']._serialized_start=433
  _globals['_TEMPLATEID']._serialized_end=465
  _globals['_TEMPLATE']._serialized_start=468
  _globals['_TEMPLATE']._serialized_end=702
  _globals['_TEMPLATE_METADATAENTRY']._serialized_start=655
  _globals['_TEMPLATE_METADATAENTRY']._serialized_end=702
  _globals['_LISTEDTEMPLATE']._serialized_start=705
  _globals['_LISTEDTEMPLATE']._serialized_end=911
  _globals['_LISTEDTEMPLATE_METADATAENTRY']._serialized_start=655
  _globals['_LISTEDTEMPLATE_METADATAENTRY']._serialized_end=702
  _globals['_GETTEMPLATE']._serialized_start=913
  _globals['_GETTEMPLATE']._serialized_end=978
  _globals['_SELECTTEMPLATES']._serialized_start=981
  _globals['_SELECTTEMPLATES']._serialized_end=1153
  _globals['_SELECTTEMPLATES_METADATAPATTERNSENTRY']._serialized_start=1098
  _globals['_SELECTTEMPLATES_METADATAPATTERNSENTRY']._serialized_end=1153
  _globals['_LISTTEMPLATES']._serialized_start=1155
  _globals['_LISTTEMPLATES']._serialized_end=1237
  _globals['_SITEID']._serialized_start=1239
  _globals['_SITEID']._serialized_end=1263
  _globals['_SITE']._serialized_start=1266
  _globals['_SITE']._serialized_end=1508
  _globals['_SITE_METADATAENTRY']._serialized_start=655
  _globals['_SITE_METADATAENTRY']._serialized_end=702
  _globals['_LISTEDSITE']._serialized_start=1511
  _globals['_LISTEDSITE']._serialized_end=1725
  _globals['_LISTEDSITE_METADATAENTRY']._serialized_start=655
  _globals['_LISTEDSITE_METADATAENTRY']._serialized_end=702
  _globals['_GETSITE']._serialized_start=1727
  _globals['_GETSITE']._serialized_end=1784
  _globals['_SELECTSITES']._serialized_start=1787
  _globals['_SELECTSITES']._serialized_end=1975
  _globals['_SELECTSITES_METADATAPATTERNSENTRY']._serialized_start=1098
  _globals['_SELECTSITES_METADATAPATTERNSENTRY']._serialized_end=1153
  _globals['_LISTSITES']._serialized_start=1977
  _globals['_LISTSITES']._serialized_end=2051
  _globals['_DEPLOYMENTID']._serialized_start=2053
  _globals['_DEPLOYMENTID']._serialized_end=2089
  _globals['_DEPLOYMENT']._serialized_start=2092
  _globals['_DEPLOYMENT']._serialized_end=2454
  _globals['_DEPLOYMENT_METADATAENTRY']._serialized_start=655
  _globals['_DEPLOYMENT_METADATAENTRY']._serialized_end=702
  _globals['_LISTEDDEPLOYMENT']._serialized_start=2457
  _globals['_LISTEDDEPLOYMENT']._serialized_end=2791
  _globals['_LISTEDDEPLOYMENT_METADATAENTRY']._serialized_start=655
  _globals['_LISTEDDEPLOYMENT_METADATAENTRY']._serialized_end=702
  _globals['_CREATEDEPLOYMENT']._serialized_start=2794
  _globals['_CREATEDEPLOYMENT']._serialized_end=3081
  _globals['_CREATEDEPLOYMENT_MERGEMETADATAENTRY']._serialized_start=3029
  _globals['_CREATEDEPLOYMENT_MERGEMETADATAENTRY']._serialized_end=3081
  _globals['_CREATEDEPLOYMENTRESPONSE']._serialized_start=3083
  _globals['_CREATEDEPLOYMENTRESPONSE']._serialized_end=3174
  _globals['_GETDEPLOYMENT']._serialized_start=3176
  _globals['_GETDEPLOYMENT']._serialized_end=3245
  _globals['_SELECTDEPLOYMENTS']._serialized_start=3248
  _globals['_SELECTDEPLOYMENTS']._serialized_end=3870
  _globals['_SELECTDEPLOYMENTS_METADATAPATTERNSENTRY']._serialized_start=1098
  _globals['_SELECTDEPLOYMENTS_METADATAPATTERNSENTRY']._serialized_end=1153
  _globals['_SELECTDEPLOYMENTS_TEMPLATEMETADATAPATTERNSENTRY']._serialized_start=3697
  _globals['_SELECTDEPLOYMENTS_TEMPLATEMETADATAPATTERNSENTRY']._serialized_end=3760
  _globals['_SELECTDEPLOYMENTS_SITEMETADATAPATTERNSENTRY']._serialized_start=3762
  _globals['_SELECTDEPLOYMENTS_SITEMETADATAPATTERNSENTRY']._serialized_end=3821
  _globals['_LISTDEPLOYMENTS']._serialized_start=3872
  _globals['_LISTDEPLOYMENTS']._serialized_end=3958
  _globals['_STARTDEPLOYMENTMODIFICATION']._serialized_start=3960
  _globals['_STARTDEPLOYMENTMODIFICATION']._serialized_end=4043
  _globals['_STARTDEPLOYMENTMODIFICATIONRESPONSE']._serialized_start=4046
  _globals['_STARTDEPLOYMENTMODIFICATIONRESPONSE']._serialized_end=4193
  _globals['_ENDDEPLOYMENTMODIFICATION']._serialized_start=4195
  _globals['_ENDDEPLOYMENTMODIFICATION']._serialized_end=4289
  _globals['_ENDDEPLOYMENTMODIFICATIONRESPONSE']._serialized_start=4291
  _globals['_ENDDEPLOYMENTMODIFICATIONRESPONSE']._serialized_end=4393
  _globals['_CANCELDEPLOYMENTMODIFICATION']._serialized_start=4395
  _globals['_CANCELDEPLOYMENTMODIFICATION']._serialized_end=4452
  _globals['_CANCELDEPLOYMENTMODIFICATIONRESPONSE']._serialized_start=4454
  _globals['_CANCELDEPLOYMENTMODIFICATIONRESPONSE']._serialized_end=4539
  _globals['_PLUGINID']._serialized_start=4541
  _globals['_PLUGINID']._serialized_end=4579
  _globals['_GVK']._serialized_start=4581
  _globals['_GVK']._serialized_end=4632
  _globals['_PLUGIN']._serialized_start=4635
  _globals['_PLUGIN']._serialized_end=4836
  _globals['_PLUGIN_PROPERTIESENTRY']._serialized_start=4787
  _globals['_PLUGIN_PROPERTIESENTRY']._serialized_end=4836
  _globals['_SELECTPLUGINS']._serialized_start=4839
  _globals['_SELECTPLUGINS']._serialized_end=4984
  _globals['_LISTPLUGINS']._serialized_start=4986
  _globals['_LISTPLUGINS']._serialized_end=5064
  _globals['_API']._serialized_start=5067
  _globals['_API']._serialized_end=6532
# @@protoc_insertion_point(module_scope)
