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

from openapi_client.models.study_version import StudyVersion  # noqa: E501

class TestStudyVersion(unittest.TestCase):
    """StudyVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyVersion:
        """Test StudyVersion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyVersion`
        """
        model = StudyVersion()  # noqa: E501
        if include_optional:
            return StudyVersion(
                id = '',
                version_identifier = '',
                rationale = '',
                abbreviations = [
                    ''
                    ],
                business_therapeutic_areas = [
                    ''
                    ],
                notes = [
                    ''
                    ],
                date_values = [
                    ''
                    ],
                reference_identifiers = [
                    ''
                    ],
                amendments = [
                    ''
                    ],
                document_versions = [
                    ''
                    ],
                study_designs = [
                    ''
                    ],
                study_identifiers = [
                    ''
                    ],
                titles = [
                    ''
                    ],
                criteria = [
                    ''
                    ],
                narrative_content_items = [
                    ''
                    ],
                roles = [
                    ''
                    ],
                organizations = [
                    ''
                    ],
                administrable_products = [
                    ''
                    ],
                medical_devices = [
                    ''
                    ],
                product_organization_roles = [
                    ''
                    ],
                instance_type = ''
            )
        else:
            return StudyVersion(
                id = '',
                version_identifier = '',
                rationale = '',
                study_identifiers = [
                    ''
                    ],
                titles = [
                    ''
                    ],
        )
        """

    def testStudyVersion(self):
        """Test StudyVersion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
