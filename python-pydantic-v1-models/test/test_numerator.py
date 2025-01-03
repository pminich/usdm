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

from openapi_client.models.numerator import Numerator  # noqa: E501

class TestNumerator(unittest.TestCase):
    """Numerator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Numerator:
        """Test Numerator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Numerator`
        """
        model = Numerator()  # noqa: E501
        if include_optional:
            return Numerator(
                id = '0',
                value = 1.337,
                unit = openapi_client.models.alias_code.AliasCode(
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
                instance_type = 'Range',
                min_value = 1.337,
                max_value = 1.337,
                is_approximate = True
            )
        else:
            return Numerator(
                id = '0',
                value = 1.337,
                instance_type = 'Range',
                min_value = 1.337,
                max_value = 1.337,
                is_approximate = True,
        )
        """

    def testNumerator(self):
        """Test Numerator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()