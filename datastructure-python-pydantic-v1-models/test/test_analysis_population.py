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

from openapi_client.models.analysis_population import AnalysisPopulation  # noqa: E501

class TestAnalysisPopulation(unittest.TestCase):
    """AnalysisPopulation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalysisPopulation:
        """Test AnalysisPopulation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalysisPopulation`
        """
        model = AnalysisPopulation()  # noqa: E501
        if include_optional:
            return AnalysisPopulation(
                id = '',
                text = '',
                name = '',
                description = '',
                label = '',
                subset_of = [
                    ''
                    ],
                notes = [
                    ''
                    ],
                instance_type = ''
            )
        else:
            return AnalysisPopulation(
                id = '',
                text = '',
                name = '',
                description = '',
                label = '',
        )
        """

    def testAnalysisPopulation(self):
        """Test AnalysisPopulation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
