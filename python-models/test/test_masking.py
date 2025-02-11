# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.masking import Masking

class TestMasking(unittest.TestCase):
    """Masking unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Masking:
        """Test Masking
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Masking`
        """
        model = Masking()
        if include_optional:
            return Masking(
                id = '0',
                description = '',
                instance_type = 'Masking'
            )
        else:
            return Masking(
                id = '0',
                description = '',
                instance_type = 'Masking',
        )
        """

    def testMasking(self):
        """Test Masking"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
