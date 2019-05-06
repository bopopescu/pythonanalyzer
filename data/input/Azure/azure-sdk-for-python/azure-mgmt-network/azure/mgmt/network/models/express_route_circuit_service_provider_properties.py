# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExpressRouteCircuitServiceProviderProperties(Model):
    """
    Contains ServiceProviderProperties in an ExpressRouteCircuit

    :param service_provider_name: Gets or sets serviceProviderName.
    :type service_provider_name: str
    :param peering_location: Gets or sets peering location.
    :type peering_location: str
    :param bandwidth_in_mbps: Gets or sets BandwidthInMbps.
    :type bandwidth_in_mbps: int
    """ 

    _attribute_map = {
        'service_provider_name': {'key': 'serviceProviderName', 'type': 'str'},
        'peering_location': {'key': 'peeringLocation', 'type': 'str'},
        'bandwidth_in_mbps': {'key': 'bandwidthInMbps', 'type': 'int'},
    }

    def __init__(self, service_provider_name=None, peering_location=None, bandwidth_in_mbps=None):
        self.service_provider_name = service_provider_name
        self.peering_location = peering_location
        self.bandwidth_in_mbps = bandwidth_in_mbps
