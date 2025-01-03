# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.study_design_population_input import StudyDesignPopulationInput

class TestStudyDesignPopulationInput(unittest.TestCase):
    """StudyDesignPopulationInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyDesignPopulationInput:
        """Test StudyDesignPopulationInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyDesignPopulationInput`
        """
        model = StudyDesignPopulationInput()
        if include_optional:
            return StudyDesignPopulationInput(
                id = '0',
                name = '0',
                label = '',
                description = '',
                includes_healthy_subjects = True,
                planned_enrollment_number = openapi_client.models.range.Range(
                    id = '0', 
                    min_value = 1.337, 
                    max_value = 1.337, 
                    unit = openapi_client.models.alias_code.AliasCode(
                        id = '0', 
                        standard_code = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        standard_code_aliases = [
                            openapi_client.models.code.Code(
                                id = '0', 
                                code = '', 
                                code_system = '', 
                                code_system_version = '', 
                                decode = '', 
                                instance_type = 'Code', )
                            ], 
                        instance_type = 'AliasCode', ), 
                    is_approximate = True, 
                    instance_type = 'Range', ),
                planned_completion_number = openapi_client.models.range.Range(
                    id = '0', 
                    min_value = 1.337, 
                    max_value = 1.337, 
                    unit = openapi_client.models.alias_code.AliasCode(
                        id = '0', 
                        standard_code = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        standard_code_aliases = [
                            openapi_client.models.code.Code(
                                id = '0', 
                                code = '', 
                                code_system = '', 
                                code_system_version = '', 
                                decode = '', 
                                instance_type = 'Code', )
                            ], 
                        instance_type = 'AliasCode', ), 
                    is_approximate = True, 
                    instance_type = 'Range', ),
                planned_sex = [
                    openapi_client.models.code.Code(
                        id = '0', 
                        code = '', 
                        code_system = '', 
                        code_system_version = '', 
                        decode = '', 
                        instance_type = 'Code', )
                    ],
                criterion_ids = [
                    ''
                    ],
                planned_age = openapi_client.models.range.Range(
                    id = '0', 
                    min_value = 1.337, 
                    max_value = 1.337, 
                    unit = openapi_client.models.alias_code.AliasCode(
                        id = '0', 
                        standard_code = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        standard_code_aliases = [
                            openapi_client.models.code.Code(
                                id = '0', 
                                code = '', 
                                code_system = '', 
                                code_system_version = '', 
                                decode = '', 
                                instance_type = 'Code', )
                            ], 
                        instance_type = 'AliasCode', ), 
                    is_approximate = True, 
                    instance_type = 'Range', ),
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
                instance_type = 'StudyDesignPopulation',
                cohorts = [
                    openapi_client.models.study_cohort.StudyCohort(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        includes_healthy_subjects = True, 
                        planned_enrollment_number = openapi_client.models.range.Range(
                            id = '0', 
                            min_value = 1.337, 
                            max_value = 1.337, 
                            unit = openapi_client.models.alias_code.AliasCode(
                                id = '0', 
                                standard_code = openapi_client.models.code.Code(
                                    id = '0', 
                                    code = '', 
                                    code_system = '', 
                                    code_system_version = '', 
                                    decode = '', 
                                    instance_type = 'Code', ), 
                                standard_code_aliases = [
                                    openapi_client.models.code.Code(
                                        id = '0', 
                                        code = '', 
                                        code_system = '', 
                                        code_system_version = '', 
                                        decode = '', 
                                        instance_type = 'Code', )
                                    ], 
                                instance_type = 'AliasCode', ), 
                            is_approximate = True, 
                            instance_type = 'Range', ), 
                        planned_completion_number = openapi_client.models.range.Range(
                            id = '0', 
                            min_value = 1.337, 
                            max_value = 1.337, 
                            is_approximate = True, 
                            instance_type = 'Range', ), 
                        planned_sex = [
                            
                            ], 
                        criterion_ids = [
                            ''
                            ], 
                        planned_age = , 
                        notes = [
                            openapi_client.models.comment_annotation.CommentAnnotation(
                                id = '0', 
                                text = '', 
                                codes = [
                                    
                                    ], 
                                instance_type = 'CommentAnnotation', )
                            ], 
                        instance_type = 'StudyCohort', 
                        characteristics = [
                            openapi_client.models.characteristic.Characteristic(
                                id = '0', 
                                name = '0', 
                                label = '', 
                                description = '', 
                                text = '', 
                                dictionary_id = '', 
                                instance_type = 'Characteristic', )
                            ], )
                    ]
            )
        else:
            return StudyDesignPopulationInput(
                id = '0',
                name = '0',
                includes_healthy_subjects = True,
                instance_type = 'StudyDesignPopulation',
        )
        """

    def testStudyDesignPopulationInput(self):
        """Test StudyDesignPopulationInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
