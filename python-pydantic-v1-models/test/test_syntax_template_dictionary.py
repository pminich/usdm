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

from openapi_client.models.syntax_template_dictionary import SyntaxTemplateDictionary  # noqa: E501

class TestSyntaxTemplateDictionary(unittest.TestCase):
    """SyntaxTemplateDictionary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyntaxTemplateDictionary:
        """Test SyntaxTemplateDictionary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyntaxTemplateDictionary`
        """
        model = SyntaxTemplateDictionary()  # noqa: E501
        if include_optional:
            return SyntaxTemplateDictionary(
                id = '0',
                name = '0',
                label = '',
                description = '',
                parameter_maps = [
                    openapi_client.models.parameter_map.ParameterMap(
                        id = '0', 
                        tag = '', 
                        reference = '', 
                        instance_type = 'ParameterMap', )
                    ],
                instance_type = 'SyntaxTemplateDictionary'
            )
        else:
            return SyntaxTemplateDictionary(
                id = '0',
                name = '0',
                parameter_maps = [
                    openapi_client.models.parameter_map.ParameterMap(
                        id = '0', 
                        tag = '', 
                        reference = '', 
                        instance_type = 'ParameterMap', )
                    ],
                instance_type = 'SyntaxTemplateDictionary',
        )
        """

    def testSyntaxTemplateDictionary(self):
        """Test SyntaxTemplateDictionary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
