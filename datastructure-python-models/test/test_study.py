# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.study import Study

class TestStudy(unittest.TestCase):
    """Study unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Study:
        """Test Study
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Study`
        """
        model = Study()
        if include_optional:
            return Study(
                id = '',
                name = '',
                description = '',
                label = '',
                versions = [
                    ''
                    ],
                documented_by = [
                    ''
                    ],
                instance_type = ''
            )
        else:
            return Study(
                id = '',
                name = '',
                description = '',
                label = '',
        )
        """

    def testStudy(self):
        """Test Study"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
