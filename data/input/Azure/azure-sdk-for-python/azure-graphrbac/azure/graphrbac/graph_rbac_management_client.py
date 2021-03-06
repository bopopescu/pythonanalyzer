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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.application_operations import ApplicationOperations
from .operations.objects_operations import ObjectsOperations
from .operations.group_operations import GroupOperations
from .operations.service_principal_operations import ServicePrincipalOperations
from .operations.user_operations import UserOperations
from . import models


class GraphRbacManagementClientConfiguration(AzureConfiguration):
    """Configuration for GraphRbacManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Gets Azure subscription credentials.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param api_version: Client Api Version.
    :type api_version: str
    :param tenant_id: Gets or sets the tenant Id.
    :type tenant_id: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, tenant_id, api_version='1.42-previewInternal', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if api_version is not None and not isinstance(api_version, str):
            raise TypeError("Optional parameter 'api_version' must be str.")
        if tenant_id is None:
            raise ValueError("Parameter 'tenant_id' must not be None.")
        if not isinstance(tenant_id, str):
            raise TypeError("Parameter 'tenant_id' must be str.")
        if accept_language is not None and not isinstance(accept_language, str):
            raise TypeError("Optional parameter 'accept_language' must be str.")
        if not base_url:
            base_url = 'https://graph.windows.net'

        super(GraphRbacManagementClientConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('graphrbacmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.api_version = api_version
        self.tenant_id = tenant_id
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class GraphRbacManagementClient(object):
    """GraphRbacManagementClient

    :param config: Configuration for client.
    :type config: GraphRbacManagementClientConfiguration

    :ivar application: Application operations
    :vartype application: .operations.ApplicationOperations
    :ivar objects: Objects operations
    :vartype objects: .operations.ObjectsOperations
    :ivar group: Group operations
    :vartype group: .operations.GroupOperations
    :ivar service_principal: ServicePrincipal operations
    :vartype service_principal: .operations.ServicePrincipalOperations
    :ivar user: User operations
    :vartype user: .operations.UserOperations
    """

    def __init__(self, config):

        self._client = ServiceClient(config.credentials, config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer()
        self._deserialize = Deserializer(client_models)

        self.config = config
        self.application = ApplicationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.objects = ObjectsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.group = GroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_principal = ServicePrincipalOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self.config, self._serialize, self._deserialize)
