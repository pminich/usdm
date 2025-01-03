# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.scheduled_decision_instance import ScheduledDecisionInstance  # noqa: E501

class TestScheduledDecisionInstance(unittest.TestCase):
    """ScheduledDecisionInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduledDecisionInstance:
        """Test ScheduledDecisionInstance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduledDecisionInstance`
        """
        model = ScheduledDecisionInstance()  # noqa: E501
        if include_optional:
            return ScheduledDecisionInstance(
                id = '0',
                name = '0',
                label = '',
                description = '',
                default_condition_id = '',
                epoch_id = '',
                instance_type = 'ScheduledDecisionInstance',
                condition_assignments = [
                    openapi_client.models.condition_assignment.ConditionAssignment(
                        id = '0', 
                        condition = '', 
                        condition_target_id = '', 
                        instance_type = 'ConditionAssignment', )
                    ]
            )
        else:
            return ScheduledDecisionInstance(
                id = '0',
                name = '0',
                instance_type = 'ScheduledDecisionInstance',
                condition_assignments = [
                    openapi_client.models.condition_assignment.ConditionAssignment(
                        id = '0', 
                        condition = '', 
                        condition_target_id = '', 
                        instance_type = 'ConditionAssignment', )
                    ],
        )
        """

    def testScheduledDecisionInstance(self):
        """Test ScheduledDecisionInstance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()