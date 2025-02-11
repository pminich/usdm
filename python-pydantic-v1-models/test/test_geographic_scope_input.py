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

from openapi_client.models.geographic_scope_input import GeographicScopeInput  # noqa: E501

class TestGeographicScopeInput(unittest.TestCase):
    """GeographicScopeInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeographicScopeInput:
        """Test GeographicScopeInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeographicScopeInput`
        """
        model = GeographicScopeInput()  # noqa: E501
        if include_optional:
            return GeographicScopeInput(
                id = '0',
                type = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                code = openapi_client.models.alias_code.AliasCode(
                    id = '0', 
                    standard_code = openapi_client.models.code.Code(
                        id = '0', 
                        code = '', 
                        code_system = '', 
                        code_system_version = '', 
                        decode = '', 
                        instance_type = 'Code', ), 
                    standard_code_aliases = [
                        openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', )
                        ], 
                    instance_type = 'AliasCode', ),
                instance_type = 'GeographicScope'
            )
        else:
            return GeographicScopeInput(
                id = '0',
                type = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                instance_type = 'GeographicScope',
        )
        """

    def testGeographicScopeInput(self):
        """Test GeographicScopeInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
