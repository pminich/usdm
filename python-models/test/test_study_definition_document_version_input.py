# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.study_definition_document_version_input import StudyDefinitionDocumentVersionInput

class TestStudyDefinitionDocumentVersionInput(unittest.TestCase):
    """StudyDefinitionDocumentVersionInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyDefinitionDocumentVersionInput:
        """Test StudyDefinitionDocumentVersionInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyDefinitionDocumentVersionInput`
        """
        model = StudyDefinitionDocumentVersionInput()
        if include_optional:
            return StudyDefinitionDocumentVersionInput(
                id = '0',
                version = '',
                status = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
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
                contents = [
                    openapi_client.models.narrative_content.NarrativeContent(
                        id = '0', 
                        name = '0', 
                        section_number = '', 
                        section_title = '', 
                        display_section_number = True, 
                        display_section_title = True, 
                        child_ids = [
                            ''
                            ], 
                        previous_id = '', 
                        next_id = '', 
                        content_item_id = '', 
                        instance_type = 'NarrativeContent', )
                    ],
                child_ids = [
                    ''
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
                instance_type = 'StudyDefinitionDocumentVersion'
            )
        else:
            return StudyDefinitionDocumentVersionInput(
                id = '0',
                version = '',
                status = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                instance_type = 'StudyDefinitionDocumentVersion',
        )
        """

    def testStudyDefinitionDocumentVersionInput(self):
        """Test StudyDefinitionDocumentVersionInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()