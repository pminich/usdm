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

from openapi_client.models.narrative_content_item import NarrativeContentItem  # noqa: E501

class TestNarrativeContentItem(unittest.TestCase):
    """NarrativeContentItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NarrativeContentItem:
        """Test NarrativeContentItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NarrativeContentItem`
        """
        model = NarrativeContentItem()  # noqa: E501
        if include_optional:
            return NarrativeContentItem(
                id = '0',
                name = '0',
                text = '',
                instance_type = 'NarrativeContentItem'
            )
        else:
            return NarrativeContentItem(
                id = '0',
                name = '0',
                text = '',
                instance_type = 'NarrativeContentItem',
        )
        """

    def testNarrativeContentItem(self):
        """Test NarrativeContentItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
