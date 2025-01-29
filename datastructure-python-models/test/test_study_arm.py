# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.study_arm import StudyArm

class TestStudyArm(unittest.TestCase):
    """StudyArm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyArm:
        """Test StudyArm
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyArm`
        """
        model = StudyArm()
        if include_optional:
            return StudyArm(
                id = '',
                name = '',
                description = '',
                label = '',
                data_origin_description = '',
                data_origin_type = '',
                type = '',
                notes = [
                    ''
                    ],
                populations = [
                    ''
                    ],
                instance_type = ''
            )
        else:
            return StudyArm(
                id = '',
                name = '',
                description = '',
                label = '',
                data_origin_description = '',
                data_origin_type = '',
                type = '',
        )
        """

    def testStudyArm(self):
        """Test StudyArm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
