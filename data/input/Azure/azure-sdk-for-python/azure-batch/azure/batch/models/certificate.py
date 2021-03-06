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


class Certificate(Model):
    """
    A certificate that can be installed on compute nodes and can be used to
    authenticate operations on the machine.

    :param thumbprint: Get or sets the X.509 thumbprint of the certificate.
     This is a sequence of up to 40 hex digits (it may include spaces but
     these are removed).
    :type thumbprint: str
    :param thumbprint_algorithm: Gets or sets the algorithm used to derive
     the thumbprint. This must be sha1.
    :type thumbprint_algorithm: str
    :param url: Gets or sets the URL of the certificate.
    :type url: str
    :param state: Gets or sets the current state of the certificate. Possible
     values include: 'active', 'deleting', 'deletefailed'
    :type state: str
    :param state_transition_time: Gets or sets the time at which the
     certificate entered its current state.
    :type state_transition_time: datetime
    :param previous_state: Gets or sets the previous state of the
     certificate. This property is not set if the certificate is in its
     initial Active state. Possible values include: 'active', 'deleting',
     'deletefailed'
    :type previous_state: str
    :param previous_state_transition_time: Gets or sets the time at which the
     certificate entered its previous state.  This property is not set if the
     certificate is in its initial Active state.
    :type previous_state_transition_time: datetime
    :param public_data: Gets or sets the public part of the certificate as a
     base-64 encoded .cer file.
    :type public_data: str
    :param delete_certificate_error: Gets or sets the error that occurred on
     the last attempt to delete this certificate.  This property is set only
     if the certificate is in the deletefailed state.
    :type delete_certificate_error: :class:`DeleteCertificateError
     <azure.batch.models.DeleteCertificateError>`
    """ 

    _attribute_map = {
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'thumbprint_algorithm': {'key': 'thumbprintAlgorithm', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'state': {'key': 'state', 'type': 'CertificateState'},
        'state_transition_time': {'key': 'stateTransitionTime', 'type': 'iso-8601'},
        'previous_state': {'key': 'previousState', 'type': 'CertificateState'},
        'previous_state_transition_time': {'key': 'previousStateTransitionTime', 'type': 'iso-8601'},
        'public_data': {'key': 'publicData', 'type': 'str'},
        'delete_certificate_error': {'key': 'deleteCertificateError', 'type': 'DeleteCertificateError'},
    }

    def __init__(self, thumbprint=None, thumbprint_algorithm=None, url=None, state=None, state_transition_time=None, previous_state=None, previous_state_transition_time=None, public_data=None, delete_certificate_error=None):
        self.thumbprint = thumbprint
        self.thumbprint_algorithm = thumbprint_algorithm
        self.url = url
        self.state = state
        self.state_transition_time = state_transition_time
        self.previous_state = previous_state
        self.previous_state_transition_time = previous_state_transition_time
        self.public_data = public_data
        self.delete_certificate_error = delete_certificate_error
