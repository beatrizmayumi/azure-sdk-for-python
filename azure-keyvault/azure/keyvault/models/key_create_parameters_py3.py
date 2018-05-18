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


class KeyCreateParameters(Model):
    """The key create parameters.

    All required parameters must be populated in order to send to Azure.

    :param kty: Required. The type of key to create. For valid values, see
     JsonWebKeyType. Possible values include: 'EC', 'EC-HSM', 'RSA', 'RSA-HSM',
     'oct'
    :type kty: str or ~azure.keyvault.models.JsonWebKeyType
    :param key_size: The key size in bits. For example, 1024 or 2048.
    :type key_size: int
    :param key_ops:
    :type key_ops: list[str or ~azure.keyvault.models.JsonWebKeyOperation]
    :param key_attributes:
    :type key_attributes: ~azure.keyvault.models.KeyAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    :param curve: Elliptic curve name. For valid values, see
     JsonWebKeyCurveName. Possible values include: 'P-256', 'P-384', 'P-521',
     'SECP256K1'
    :type curve: str or ~azure.keyvault.models.JsonWebKeyCurveName
    """

    _validation = {
        'kty': {'required': True, 'min_length': 1},
    }

    _attribute_map = {
        'kty': {'key': 'kty', 'type': 'str'},
        'key_size': {'key': 'key_size', 'type': 'int'},
        'key_ops': {'key': 'key_ops', 'type': '[str]'},
        'key_attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'curve': {'key': 'crv', 'type': 'str'},
    }

    def __init__(self, *, kty, key_size: int=None, key_ops=None, key_attributes=None, tags=None, curve=None, **kwargs) -> None:
        super(KeyCreateParameters, self).__init__(**kwargs)
        self.kty = kty
        self.key_size = key_size
        self.key_ops = key_ops
        self.key_attributes = key_attributes
        self.tags = tags
        self.curve = curve
