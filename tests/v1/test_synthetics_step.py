# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_step_type
except ImportError:
    synthetics_step_type = sys.modules[
        'datadog_api_client.v1.model.synthetics_step_type']
from datadog_api_client.v1.model.synthetics_step import SyntheticsStep


class TestSyntheticsStep(unittest.TestCase):
    """SyntheticsStep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsStep(self):
        """Test SyntheticsStep"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsStep()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
