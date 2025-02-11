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

from openapi_client.models.narrative_content import NarrativeContent  # noqa: E501

class TestNarrativeContent(unittest.TestCase):
    """NarrativeContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NarrativeContent:
        """Test NarrativeContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NarrativeContent`
        """
        model = NarrativeContent()  # noqa: E501
        if include_optional:
            return NarrativeContent(
                id = '',
                name = '',
                section_number = '',
                section_title = '',
                display_section_title = '',
                display_section_number = '',
                content_item = '',
                previous = '',
                next = '',
                children = [
                    ''
                    ],
                instance_type = ''
            )
        else:
            return NarrativeContent(
                id = '',
                name = '',
                section_number = '',
                section_title = '',
                display_section_title = '',
                display_section_number = '',
        )
        """

    def testNarrativeContent(self):
        """Test NarrativeContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
