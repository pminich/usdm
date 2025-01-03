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

from openapi_client.models.study_change import StudyChange  # noqa: E501

class TestStudyChange(unittest.TestCase):
    """StudyChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyChange:
        """Test StudyChange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyChange`
        """
        model = StudyChange()  # noqa: E501
        if include_optional:
            return StudyChange(
                id = '0',
                name = '0',
                label = '',
                description = '',
                summary = '',
                rationale = '',
                changed_sections = [
                    openapi_client.models.document_content_reference.DocumentContentReference(
                        id = '0', 
                        section_number = '', 
                        section_title = '', 
                        applies_to_id = '', 
                        instance_type = 'DocumentContentReference', )
                    ],
                instance_type = 'StudyChange'
            )
        else:
            return StudyChange(
                id = '0',
                name = '0',
                summary = '',
                rationale = '',
                changed_sections = [
                    openapi_client.models.document_content_reference.DocumentContentReference(
                        id = '0', 
                        section_number = '', 
                        section_title = '', 
                        applies_to_id = '', 
                        instance_type = 'DocumentContentReference', )
                    ],
                instance_type = 'StudyChange',
        )
        """

    def testStudyChange(self):
        """Test StudyChange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
