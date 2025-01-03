# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.numerator1 import Numerator1

class TestNumerator1(unittest.TestCase):
    """Numerator1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Numerator1:
        """Test Numerator1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Numerator1`
        """
        model = Numerator1()
        if include_optional:
            return Numerator1(
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
            return Numerator1(
                id = '0',
                value = 1.337,
                instance_type = 'Range',
                min_value = 1.337,
                max_value = 1.337,
                is_approximate = True,
        )
        """

    def testNumerator1(self):
        """Test Numerator1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
