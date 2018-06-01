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

from msrest.serialization import Model


class VaultPatchProperties(Model):
    """Properties of the vault.

    :param tenant_id: The Azure Active Directory tenant ID that should be used
     for authenticating requests to the key vault.
    :type tenant_id: str
    :param sku: SKU details
    :type sku: ~azure.mgmt.keyvault.models.Sku
    :param access_policies: An array of 0 to 16 identities that have access to
     the key vault. All identities in the array must use the same tenant ID as
     the key vault's tenant ID.
    :type access_policies: list[~azure.mgmt.keyvault.models.AccessPolicyEntry]
    :param enabled_for_deployment: Property to specify whether Azure Virtual
     Machines are permitted to retrieve certificates stored as secrets from the
     key vault.
    :type enabled_for_deployment: bool
    :param enabled_for_disk_encryption: Property to specify whether Azure Disk
     Encryption is permitted to retrieve secrets from the vault and unwrap
     keys.
    :type enabled_for_disk_encryption: bool
    :param enabled_for_template_deployment: Property to specify whether Azure
     Resource Manager is permitted to retrieve secrets from the key vault.
    :type enabled_for_template_deployment: bool
    :param enable_soft_delete: Property specifying whether recoverable
     deletion ('soft' delete) is enabled for this key vault. The property may
     not be set to false.
    :type enable_soft_delete: bool
    :param create_mode: The vault's create mode to indicate whether the vault
     need to be recovered or not. Possible values include: 'recover', 'default'
    :type create_mode: str or ~azure.mgmt.keyvault.models.CreateMode
    :param enable_purge_protection: Property specifying whether protection
     against purge is enabled for this vault; it is only effective if soft
     delete is also enabled. Once activated, the property may no longer be
     reset to false.
    :type enable_purge_protection: bool
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'access_policies': {'key': 'accessPolicies', 'type': '[AccessPolicyEntry]'},
        'enabled_for_deployment': {'key': 'enabledForDeployment', 'type': 'bool'},
        'enabled_for_disk_encryption': {'key': 'enabledForDiskEncryption', 'type': 'bool'},
        'enabled_for_template_deployment': {'key': 'enabledForTemplateDeployment', 'type': 'bool'},
        'enable_soft_delete': {'key': 'enableSoftDelete', 'type': 'bool'},
        'create_mode': {'key': 'createMode', 'type': 'CreateMode'},
        'enable_purge_protection': {'key': 'enablePurgeProtection', 'type': 'bool'},
    }

    def __init__(self, *, tenant_id: str=None, sku=None, access_policies=None, enabled_for_deployment: bool=None, enabled_for_disk_encryption: bool=None, enabled_for_template_deployment: bool=None, enable_soft_delete: bool=None, create_mode=None, enable_purge_protection: bool=None, **kwargs) -> None:
        super(VaultPatchProperties, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.sku = sku
        self.access_policies = access_policies
        self.enabled_for_deployment = enabled_for_deployment
        self.enabled_for_disk_encryption = enabled_for_disk_encryption
        self.enabled_for_template_deployment = enabled_for_template_deployment
        self.enable_soft_delete = enable_soft_delete
        self.create_mode = create_mode
        self.enable_purge_protection = enable_purge_protection