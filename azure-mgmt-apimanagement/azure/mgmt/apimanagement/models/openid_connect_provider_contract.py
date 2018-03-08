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

from .resource import Resource


class OpenidConnectProviderContract(Resource):
    """OpenId Connect Provider details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param display_name: Required. User-friendly OpenID Connect Provider name.
    :type display_name: str
    :param description: User-friendly description of OpenID Connect Provider.
    :type description: str
    :param metadata_endpoint: Required. Metadata endpoint URI.
    :type metadata_endpoint: str
    :param client_id: Required. Client ID of developer console which is the
     client application.
    :type client_id: str
    :param client_secret: Client Secret of developer console which is the
     client application.
    :type client_secret: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'required': True, 'max_length': 50},
        'metadata_endpoint': {'required': True},
        'client_id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata_endpoint': {'key': 'properties.metadataEndpoint', 'type': 'str'},
        'client_id': {'key': 'properties.clientId', 'type': 'str'},
        'client_secret': {'key': 'properties.clientSecret', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OpenidConnectProviderContract, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.metadata_endpoint = kwargs.get('metadata_endpoint', None)
        self.client_id = kwargs.get('client_id', None)
        self.client_secret = kwargs.get('client_secret', None)