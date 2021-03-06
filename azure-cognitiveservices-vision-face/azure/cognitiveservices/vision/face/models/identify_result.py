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


class IdentifyResult(Model):
    """Response body for identify face operation.

    :param face_id: FaceId of the query face
    :type face_id: str
    :param candidates: Identified person candidates for that face (ranked by
     confidence). Array size should be no larger than input
     maxNumOfCandidatesReturned. If no person is identified, will return an
     empty array.
    :type candidates:
     list[~azure.cognitiveservices.vision.face.models.IdentifyCandidate]
    """

    _validation = {
        'face_id': {'required': True},
        'candidates': {'required': True},
    }

    _attribute_map = {
        'face_id': {'key': 'faceId', 'type': 'str'},
        'candidates': {'key': 'candidates', 'type': '[IdentifyCandidate]'},
    }

    def __init__(self, face_id, candidates):
        super(IdentifyResult, self).__init__()
        self.face_id = face_id
        self.candidates = candidates
