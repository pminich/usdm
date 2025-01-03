# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.condition_assignment import ConditionAssignment

class TestConditionAssignment(unittest.TestCase):
    """ConditionAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConditionAssignment:
        """Test ConditionAssignment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConditionAssignment`
        """
        model = ConditionAssignment()
        if include_optional:
            return ConditionAssignment(
                id = '0',
                condition = '',
                condition_target_id = '',
                instance_type = 'ConditionAssignment'
            )
        else:
            return ConditionAssignment(
                id = '0',
                condition = '',
                condition_target_id = '',
                instance_type = 'ConditionAssignment',
        )
        """

    def testConditionAssignment(self):
        """Test ConditionAssignment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
