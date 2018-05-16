# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .gallery_identifier_py3 import GalleryIdentifier
    from .gallery_py3 import Gallery
    from .gallery_image_identifier_py3 import GalleryImageIdentifier
    from .resource_range_py3 import ResourceRange
    from .recommended_machine_configuration_py3 import RecommendedMachineConfiguration
    from .disallowed_py3 import Disallowed
    from .image_purchase_plan_py3 import ImagePurchasePlan
    from .gallery_image_py3 import GalleryImage
    from .gallery_image_version_publishing_profile_py3 import GalleryImageVersionPublishingProfile
    from .gallery_os_disk_image_py3 import GalleryOSDiskImage
    from .gallery_data_disk_image_py3 import GalleryDataDiskImage
    from .gallery_image_version_storage_profile_py3 import GalleryImageVersionStorageProfile
    from .regional_replication_status_py3 import RegionalReplicationStatus
    from .replication_status_py3 import ReplicationStatus
    from .gallery_image_version_py3 import GalleryImageVersion
    from .managed_artifact_py3 import ManagedArtifact
    from .gallery_artifact_source_py3 import GalleryArtifactSource
    from .gallery_artifact_publishing_profile_base_py3 import GalleryArtifactPublishingProfileBase
    from .gallery_disk_image_py3 import GalleryDiskImage
    from .gallery_list_py3 import GalleryList
    from .gallery_image_list_py3 import GalleryImageList
    from .gallery_image_version_list_py3 import GalleryImageVersionList
    from .resource_py3 import Resource
except (SyntaxError, ImportError):
    from .gallery_identifier import GalleryIdentifier
    from .gallery import Gallery
    from .gallery_image_identifier import GalleryImageIdentifier
    from .resource_range import ResourceRange
    from .recommended_machine_configuration import RecommendedMachineConfiguration
    from .disallowed import Disallowed
    from .image_purchase_plan import ImagePurchasePlan
    from .gallery_image import GalleryImage
    from .gallery_image_version_publishing_profile import GalleryImageVersionPublishingProfile
    from .gallery_os_disk_image import GalleryOSDiskImage
    from .gallery_data_disk_image import GalleryDataDiskImage
    from .gallery_image_version_storage_profile import GalleryImageVersionStorageProfile
    from .regional_replication_status import RegionalReplicationStatus
    from .replication_status import ReplicationStatus
    from .gallery_image_version import GalleryImageVersion
    from .managed_artifact import ManagedArtifact
    from .gallery_artifact_source import GalleryArtifactSource
    from .gallery_artifact_publishing_profile_base import GalleryArtifactPublishingProfileBase
    from .gallery_disk_image import GalleryDiskImage
    from .gallery_list import GalleryList
    from .gallery_image_list import GalleryImageList
    from .gallery_image_version_list import GalleryImageVersionList
    from .resource import Resource
from .compute_management_client_enums import (
    OperatingSystemTypes,
    OperatingSystemStateTypes,
    AggregatedReplicationState,
    ReplicationState,
    HostCaching,
)

__all__ = [
    'GalleryIdentifier',
    'Gallery',
    'GalleryImageIdentifier',
    'ResourceRange',
    'RecommendedMachineConfiguration',
    'Disallowed',
    'ImagePurchasePlan',
    'GalleryImage',
    'GalleryImageVersionPublishingProfile',
    'GalleryOSDiskImage',
    'GalleryDataDiskImage',
    'GalleryImageVersionStorageProfile',
    'RegionalReplicationStatus',
    'ReplicationStatus',
    'GalleryImageVersion',
    'ManagedArtifact',
    'GalleryArtifactSource',
    'GalleryArtifactPublishingProfileBase',
    'GalleryDiskImage',
    'GalleryList',
    'GalleryImageList',
    'GalleryImageVersionList',
    'Resource',
    'OperatingSystemTypes',
    'OperatingSystemStateTypes',
    'AggregatedReplicationState',
    'ReplicationState',
    'HostCaching',
]