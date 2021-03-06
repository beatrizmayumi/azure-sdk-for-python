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


class PagedSubNameInfoList(Model):
    """A paged list of Service Fabric names. The list is paged when all of the
    results cannot fit in a single message. The next set of results can be
    obtained by executing the same query with the continuation token provided
    in this list.

    :param continuation_token: The continuation token parameter is used to
     obtain next set of results. The continuation token is included in the
     response of the API when the results from the system do not fit in a
     single response. When this value is passed to the next API call, the API
     returns next set of results. If there are no further results then the
     continuation token is not included in the response.
    :type continuation_token: str
    :param is_consistent: Indicates whether any name under the given name has
     been modified during the enumeration. If there was a modification, this
     property value is false.
    :type is_consistent: bool
    :param sub_names: List of the child names.
    :type sub_names: list[str]
    """

    _attribute_map = {
        'continuation_token': {'key': 'ContinuationToken', 'type': 'str'},
        'is_consistent': {'key': 'IsConsistent', 'type': 'bool'},
        'sub_names': {'key': 'SubNames', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(PagedSubNameInfoList, self).__init__(**kwargs)
        self.continuation_token = kwargs.get('continuation_token', None)
        self.is_consistent = kwargs.get('is_consistent', None)
        self.sub_names = kwargs.get('sub_names', None)
