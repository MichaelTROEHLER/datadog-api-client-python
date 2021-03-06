# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_browser_error
except ImportError:
    synthetics_browser_error = sys.modules[
        'datadog_api_client.v1.model.synthetics_browser_error']
try:
    from datadog_api_client.v1.model import synthetics_check_type
except ImportError:
    synthetics_check_type = sys.modules[
        'datadog_api_client.v1.model.synthetics_check_type']
try:
    from datadog_api_client.v1.model import synthetics_playing_tab
except ImportError:
    synthetics_playing_tab = sys.modules[
        'datadog_api_client.v1.model.synthetics_playing_tab']
try:
    from datadog_api_client.v1.model import synthetics_resource
except ImportError:
    synthetics_resource = sys.modules[
        'datadog_api_client.v1.model.synthetics_resource']
try:
    from datadog_api_client.v1.model import synthetics_step_detail_warnings
except ImportError:
    synthetics_step_detail_warnings = sys.modules[
        'datadog_api_client.v1.model.synthetics_step_detail_warnings']
try:
    from datadog_api_client.v1.model import synthetics_step_type
except ImportError:
    synthetics_step_type = sys.modules[
        'datadog_api_client.v1.model.synthetics_step_type']
from datadog_api_client.v1.model.synthetics_step_detail import SyntheticsStepDetail


class TestSyntheticsStepDetail(unittest.TestCase):
    """SyntheticsStepDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsStepDetail(self):
        """Test SyntheticsStepDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsStepDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
