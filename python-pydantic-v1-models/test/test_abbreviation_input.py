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

from openapi_client.models.abbreviation_input import AbbreviationInput  # noqa: E501

class TestAbbreviationInput(unittest.TestCase):
    """AbbreviationInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AbbreviationInput:
        """Test AbbreviationInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AbbreviationInput`
        """
        model = AbbreviationInput()  # noqa: E501
        if include_optional:
            return AbbreviationInput(
                id = '0',
                abbreviated_text = '0',
                expanded_text = '0',
                notes = [
                    openapi_client.models.comment_annotation.CommentAnnotation(
                        id = '0', 
                        text = '', 
                        codes = [
                            openapi_client.models.code.Code(
                                id = '0', 
                                code = '', 
                                code_system = '', 
                                code_system_version = '', 
                                decode = '', 
                                instance_type = 'Code', )
                            ], 
                        instance_type = 'CommentAnnotation', )
                    ],
                instance_type = 'Abbreviation'
            )
        else:
            return AbbreviationInput(
                id = '0',
                abbreviated_text = '0',
                expanded_text = '0',
                instance_type = 'Abbreviation',
        )
        """

    def testAbbreviationInput(self):
        """Test AbbreviationInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
