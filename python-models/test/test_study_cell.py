# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.study_cell import StudyCell

class TestStudyCell(unittest.TestCase):
    """StudyCell unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyCell:
        """Test StudyCell
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyCell`
        """
        model = StudyCell()
        if include_optional:
            return StudyCell(
                id = '0',
                arm_id = '',
                epoch_id = '',
                element_ids = [
                    ''
                    ],
                instance_type = 'StudyCell'
            )
        else:
            return StudyCell(
                id = '0',
                arm_id = '',
                epoch_id = '',
                instance_type = 'StudyCell',
        )
        """

    def testStudyCell(self):
        """Test StudyCell"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
