# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.schedule_timeline_exit import ScheduleTimelineExit

class TestScheduleTimelineExit(unittest.TestCase):
    """ScheduleTimelineExit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleTimelineExit:
        """Test ScheduleTimelineExit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleTimelineExit`
        """
        model = ScheduleTimelineExit()
        if include_optional:
            return ScheduleTimelineExit(
                id = '',
                instance_type = ''
            )
        else:
            return ScheduleTimelineExit(
                id = '',
        )
        """

    def testScheduleTimelineExit(self):
        """Test ScheduleTimelineExit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
