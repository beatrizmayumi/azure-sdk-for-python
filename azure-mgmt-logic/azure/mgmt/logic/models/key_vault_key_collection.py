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


class KeyVaultKeyCollection(Model):
    """Collection of key vault keys.

    :param value: The key vault keys.
    :type value: list[~azure.mgmt.logic.models.KeyVaultKey]
    :param skip_token: The skip token.
    :type skip_token: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[KeyVaultKey]'},
        'skip_token': {'key': 'skipToken', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(KeyVaultKeyCollection, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.skip_token = kwargs.get('skip_token', None)