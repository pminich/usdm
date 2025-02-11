# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.study_element import StudyElement  # noqa: E501

class TestStudyElement(unittest.TestCase):
    """StudyElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyElement:
        """Test StudyElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyElement`
        """
        model = StudyElement()  # noqa: E501
        if include_optional:
            return StudyElement(
                id = '',
                name = '',
                description = '',
                label = '',
                notes = [
                    ''
                    ],
                transition_end_rule = '',
                study_interventions = [
                    ''
                    ],
                transition_start_rule = '',
                instance_type = ''
            )
        else:
            return StudyElement(
                id = '',
                name = '',
                description = '',
                label = '',
        )
        """

    def testStudyElement(self):
        """Test StudyElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
