# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.scheduled_decision_instance import ScheduledDecisionInstance

class TestScheduledDecisionInstance(unittest.TestCase):
    """ScheduledDecisionInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduledDecisionInstance:
        """Test ScheduledDecisionInstance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduledDecisionInstance`
        """
        model = ScheduledDecisionInstance()
        if include_optional:
            return ScheduledDecisionInstance(
                id = '',
                name = '',
                description = '',
                label = '',
                default_condition = '',
                epoch = '',
                condition_assignments = [
                    ''
                    ],
                instance_type = ''
            )
        else:
            return ScheduledDecisionInstance(
                id = '',
                name = '',
                description = '',
                label = '',
                condition_assignments = [
                    ''
                    ],
        )
        """

    def testScheduledDecisionInstance(self):
        """Test ScheduledDecisionInstance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
