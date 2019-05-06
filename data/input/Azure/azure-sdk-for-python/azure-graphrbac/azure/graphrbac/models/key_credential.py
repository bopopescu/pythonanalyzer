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


class KeyCredential(Model):
    """
    Active Directory service principal Key Credential information

    :param start_date: Gets or sets start date
    :type start_date: datetime
    :param end_date: Gets or sets end date
    :type end_date: datetime
    :param value: Gets or sets value
    :type value: str
    :param key_id: Gets or sets key Id
    :type key_id: str
    :param usage: Gets or sets usage
    :type usage: str
    :param type: Gets or sets type
    :type type: str
    """ 

    _attribute_map = {
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'str'},
        'key_id': {'key': 'keyId', 'type': 'str'},
        'usage': {'key': 'usage', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, start_date=None, end_date=None, value=None, key_id=None, usage=None, type=None):
        self.start_date = start_date
        self.end_date = end_date
        self.value = value
        self.key_id = key_id
        self.usage = usage
        self.type = type
