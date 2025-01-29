# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.biospecimen_retention import BiospecimenRetention  # noqa: E501

class TestBiospecimenRetention(unittest.TestCase):
    """BiospecimenRetention unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BiospecimenRetention:
        """Test BiospecimenRetention
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BiospecimenRetention`
        """
        model = BiospecimenRetention()  # noqa: E501
        if include_optional:
            return BiospecimenRetention(
                id = '',
                name = '',
                description = '',
                label = '',
                is_retained = '',
                includes_dna = '',
                instance_type = ''
            )
        else:
            return BiospecimenRetention(
                id = '',
                name = '',
                description = '',
                label = '',
                is_retained = '',
                includes_dna = '',
        )
        """

    def testBiospecimenRetention(self):
        """Test BiospecimenRetention"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
