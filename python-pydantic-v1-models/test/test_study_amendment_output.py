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

from openapi_client.models.study_amendment_output import StudyAmendmentOutput  # noqa: E501

class TestStudyAmendmentOutput(unittest.TestCase):
    """StudyAmendmentOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyAmendmentOutput:
        """Test StudyAmendmentOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyAmendmentOutput`
        """
        model = StudyAmendmentOutput()  # noqa: E501
        if include_optional:
            return StudyAmendmentOutput(
                id = '0',
                number = '',
                summary = '',
                primary_reason = openapi_client.models.study_amendment_reason.StudyAmendmentReason(
                    id = '0', 
                    code = openapi_client.models.code.Code(
                        id = '0', 
                        code = '', 
                        code_system = '', 
                        code_system_version = '', 
                        decode = '', 
                        instance_type = 'Code', ), 
                    other_reason = '', 
                    instance_type = 'StudyAmendmentReason', ),
                secondary_reasons = [
                    openapi_client.models.study_amendment_reason.StudyAmendmentReason(
                        id = '0', 
                        code = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        other_reason = '', 
                        instance_type = 'StudyAmendmentReason', )
                    ],
                changes = [
                    openapi_client.models.study_change.StudyChange(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        summary = '', 
                        rationale = '', 
                        changed_sections = [
                            openapi_client.models.document_content_reference.DocumentContentReference(
                                id = '0', 
                                section_number = '', 
                                section_title = '', 
                                applies_to_id = '', 
                                instance_type = 'DocumentContentReference', )
                            ], 
                        instance_type = 'StudyChange', )
                    ],
                impacts = [
                    openapi_client.models.study_amendment_impact.StudyAmendmentImpact(
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
                        instance_type = 'StudyAmendmentImpact', )
                    ],
                geographic_scopes = [
                    openapi_client.models.geographic_scope.GeographicScope(
                        id = '0', 
                        type = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        code = openapi_client.models.alias_code.AliasCode(
                            id = '0', 
                            standard_code = openapi_client.models.code.Code(
                                id = '0', 
                                code = '', 
                                code_system = '', 
                                code_system_version = '', 
                                decode = '', 
                                instance_type = 'Code', ), 
                            standard_code_aliases = [
                                
                                ], 
                            instance_type = 'AliasCode', ), 
                        instance_type = 'GeographicScope', )
                    ],
                enrollments = [
                    openapi_client.models.subject_enrollment.SubjectEnrollment(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        quantity = openapi_client.models.quantity.Quantity(
                            id = '0', 
                            value = 1.337, 
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
                            instance_type = 'Quantity', ), 
                        applies_to = openapi_client.models.geographic_scope.GeographicScope(
                            id = '0', 
                            type = , 
                            instance_type = 'GeographicScope', ), 
                        applies_to_id = '', 
                        instance_type = 'SubjectEnrollment', )
                    ],
                date_values = [
                    openapi_client.models.governance_date.GovernanceDate(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        type = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        date_value = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        geographic_scopes = [
                            openapi_client.models.geographic_scope.GeographicScope(
                                id = '0', 
                                type = openapi_client.models.code.Code(
                                    id = '0', 
                                    code = '', 
                                    code_system = '', 
                                    code_system_version = '', 
                                    decode = '', 
                                    instance_type = 'Code', ), 
                                instance_type = 'GeographicScope', )
                            ], 
                        instance_type = 'GovernanceDate', )
                    ],
                previous_id = '',
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
                instance_type = 'StudyAmendment'
            )
        else:
            return StudyAmendmentOutput(
                id = '0',
                number = '',
                summary = '',
                primary_reason = openapi_client.models.study_amendment_reason.StudyAmendmentReason(
                    id = '0', 
                    code = openapi_client.models.code.Code(
                        id = '0', 
                        code = '', 
                        code_system = '', 
                        code_system_version = '', 
                        decode = '', 
                        instance_type = 'Code', ), 
                    other_reason = '', 
                    instance_type = 'StudyAmendmentReason', ),
                changes = [
                    openapi_client.models.study_change.StudyChange(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        summary = '', 
                        rationale = '', 
                        changed_sections = [
                            openapi_client.models.document_content_reference.DocumentContentReference(
                                id = '0', 
                                section_number = '', 
                                section_title = '', 
                                applies_to_id = '', 
                                instance_type = 'DocumentContentReference', )
                            ], 
                        instance_type = 'StudyChange', )
                    ],
                geographic_scopes = [
                    openapi_client.models.geographic_scope.GeographicScope(
                        id = '0', 
                        type = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        code = openapi_client.models.alias_code.AliasCode(
                            id = '0', 
                            standard_code = openapi_client.models.code.Code(
                                id = '0', 
                                code = '', 
                                code_system = '', 
                                code_system_version = '', 
                                decode = '', 
                                instance_type = 'Code', ), 
                            standard_code_aliases = [
                                
                                ], 
                            instance_type = 'AliasCode', ), 
                        instance_type = 'GeographicScope', )
                    ],
                instance_type = 'StudyAmendment',
        )
        """

    def testStudyAmendmentOutput(self):
        """Test StudyAmendmentOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
