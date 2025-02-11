# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.study_amendment_impact_output import StudyAmendmentImpactOutput

class TestStudyAmendmentImpactOutput(unittest.TestCase):
    """StudyAmendmentImpactOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyAmendmentImpactOutput:
        """Test StudyAmendmentImpactOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyAmendmentImpactOutput`
        """
        model = StudyAmendmentImpactOutput()
        if include_optional:
            return StudyAmendmentImpactOutput(
                id = '0',
                type = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                text = '',
                is_substantial = True,
                notes = [
                    openapi_client.models.comment_annotation.CommentAnnotation(
                        id = '0', 
                        text = '', 
                        codes = [
                            openapi_client.models.code.Code(
                                id = '0', 
                                code = '', 
                                code_system = '', 
                                code_system_version = '', 
                                decode = '', 
                                instance_type = 'Code', )
                            ], 
                        instance_type = 'CommentAnnotation', )
                    ],
                instance_type = 'StudyAmendmentImpact'
            )
        else:
            return StudyAmendmentImpactOutput(
                id = '0',
                type = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                text = '',
                is_substantial = True,
                instance_type = 'StudyAmendmentImpact',
        )
        """

    def testStudyAmendmentImpactOutput(self):
        """Test StudyAmendmentImpactOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
