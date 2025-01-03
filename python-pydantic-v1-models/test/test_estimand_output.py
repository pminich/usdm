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

from openapi_client.models.estimand_output import EstimandOutput  # noqa: E501

class TestEstimandOutput(unittest.TestCase):
    """EstimandOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimandOutput:
        """Test EstimandOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimandOutput`
        """
        model = EstimandOutput()  # noqa: E501
        if include_optional:
            return EstimandOutput(
                id = '0',
                name = '0',
                label = '',
                description = '',
                population_summary = '',
                analysis_population_id = '',
                intervention_ids = [
                    ''
                    ],
                variable_of_interest_id = '',
                intercurrent_events = [
                    openapi_client.models.intercurrent_event.IntercurrentEvent(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        text = '', 
                        dictionary_id = '', 
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
                        instance_type = 'IntercurrentEvent', 
                        strategy = '', )
                    ],
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
                instance_type = 'Estimand'
            )
        else:
            return EstimandOutput(
                id = '0',
                name = '0',
                population_summary = '',
                analysis_population_id = '',
                intervention_ids = [
                    ''
                    ],
                variable_of_interest_id = '',
                intercurrent_events = [
                    openapi_client.models.intercurrent_event.IntercurrentEvent(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        text = '', 
                        dictionary_id = '', 
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
                        instance_type = 'IntercurrentEvent', 
                        strategy = '', )
                    ],
                instance_type = 'Estimand',
        )
        """

    def testEstimandOutput(self):
        """Test EstimandOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
