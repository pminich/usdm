# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.code import Code

class TestCode(unittest.TestCase):
    """Code unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Code:
        """Test Code
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Code`
        """
        model = Code()
        if include_optional:
            return Code(
                id = '0',
                code = '',
                code_system = '',
                code_system_version = '',
                decode = '',
                instance_type = 'Code'
            )
        else:
            return Code(
                id = '0',
                code = '',
                code_system = '',
                code_system_version = '',
                decode = '',
                instance_type = 'Code',
        )
        """

    def testCode(self):
        """Test Code"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
