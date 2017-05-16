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

from .replicator_status import ReplicatorStatus


class PrimaryReplicatorStatus(ReplicatorStatus):
    """PrimaryReplicatorStatus.

    :param Kind: Polymorphic Discriminator
    :type Kind: str
    :param replication_queue_status: Details about the replication queue on
     the primary replicator.
    :type replication_queue_status: :class:`ReplicatorQueueStatus
     <azure.servicefabric.models.ReplicatorQueueStatus>`
    :param remote_replicators: The status of all the active and idle
     secondary replicators that the primary is aware of.
    :type remote_replicators: list of :class:`RemoteReplicatorStatus
     <azure.servicefabric.models.RemoteReplicatorStatus>`
    """ 

    _validation = {
        'Kind': {'required': True},
    }

    _attribute_map = {
        'Kind': {'key': 'Kind', 'type': 'str'},
        'replication_queue_status': {'key': 'ReplicationQueueStatus', 'type': 'ReplicatorQueueStatus'},
        'remote_replicators': {'key': 'RemoteReplicators', 'type': '[RemoteReplicatorStatus]'},
    }

    def __init__(self, replication_queue_status=None, remote_replicators=None):
        super(PrimaryReplicatorStatus, self).__init__()
        self.replication_queue_status = replication_queue_status
        self.remote_replicators = remote_replicators
        self.Kind = 'Primary'