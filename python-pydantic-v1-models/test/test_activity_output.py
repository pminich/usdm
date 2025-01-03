# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.activity_output import ActivityOutput  # noqa: E501

class TestActivityOutput(unittest.TestCase):
    """ActivityOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityOutput:
        """Test ActivityOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityOutput`
        """
        model = ActivityOutput()  # noqa: E501
        if include_optional:
            return ActivityOutput(
                id = '0',
                name = '0',
                label = '',
                description = '',
                previous_id = '',
                next_id = '',
                child_ids = [
                    ''
                    ],
                defined_procedures = [
                    openapi_client.models.procedure.Procedure(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        procedure_type = '', 
                        code = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        study_intervention_id = '', 
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
                        instance_type = 'Procedure', )
                    ],
                biomedical_concept_ids = [
                    ''
                    ],
                bc_category_ids = [
                    ''
                    ],
                bc_surrogate_ids = [
                    ''
                    ],
                timeline_id = '',
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
                instance_type = 'Activity'
            )
        else:
            return ActivityOutput(
                id = '0',
                name = '0',
                instance_type = 'Activity',
        )
        """

    def testActivityOutput(self):
        """Test ActivityOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
