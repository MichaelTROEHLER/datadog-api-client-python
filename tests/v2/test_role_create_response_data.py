# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import role_create_attributes
except ImportError:
    role_create_attributes = sys.modules[
        'datadog_api_client.v2.model.role_create_attributes']
try:
    from datadog_api_client.v2.model import role_response_relationships
except ImportError:
    role_response_relationships = sys.modules[
        'datadog_api_client.v2.model.role_response_relationships']
try:
    from datadog_api_client.v2.model import roles_type
except ImportError:
    roles_type = sys.modules[
        'datadog_api_client.v2.model.roles_type']
from datadog_api_client.v2.model.role_create_response_data import RoleCreateResponseData


class TestRoleCreateResponseData(unittest.TestCase):
    """RoleCreateResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleCreateResponseData(self):
        """Test RoleCreateResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleCreateResponseData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
