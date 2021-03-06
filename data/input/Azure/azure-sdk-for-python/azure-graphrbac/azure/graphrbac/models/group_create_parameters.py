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


class GroupCreateParameters(Model):
    """
    Request parameters for create a new group

    :param display_name: Group display name
    :type display_name: str
    :param mail_enabled: Mail
    :type mail_enabled: bool
    :param mail_nickname: Mail nick name
    :type mail_nickname: str
    :param security_enabled: Is security enabled
    :type security_enabled: bool
    """ 

    _validation = {
        'display_name': {'required': True},
        'mail_enabled': {'required': True},
        'mail_nickname': {'required': True},
        'security_enabled': {'required': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'mail_enabled': {'key': 'mailEnabled', 'type': 'bool'},
        'mail_nickname': {'key': 'mailNickname', 'type': 'str'},
        'security_enabled': {'key': 'securityEnabled', 'type': 'bool'},
    }

    def __init__(self, display_name, mail_enabled, mail_nickname, security_enabled):
        self.display_name = display_name
        self.mail_enabled = mail_enabled
        self.mail_nickname = mail_nickname
        self.security_enabled = security_enabled
