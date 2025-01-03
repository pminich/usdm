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

from openapi_client.models.encounter_input import EncounterInput  # noqa: E501

class TestEncounterInput(unittest.TestCase):
    """EncounterInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EncounterInput:
        """Test EncounterInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EncounterInput`
        """
        model = EncounterInput()  # noqa: E501
        if include_optional:
            return EncounterInput(
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
                previous_id = '',
                next_id = '',
                scheduled_at_id = '',
                environmental_settings = [
                    openapi_client.models.code.Code(
                        id = '0', 
                        code = '', 
                        code_system = '', 
                        code_system_version = '', 
                        decode = '', 
                        instance_type = 'Code', )
                    ],
                contact_modes = [
                    openapi_client.models.code.Code(
                        id = '0', 
                        code = '', 
                        code_system = '', 
                        code_system_version = '', 
                        decode = '', 
                        instance_type = 'Code', )
                    ],
                transition_start_rule = openapi_client.models.transition_rule.TransitionRule(
                    id = '0', 
                    name = '0', 
                    label = '', 
                    description = '', 
                    text = '', 
                    instance_type = 'TransitionRule', ),
                transition_end_rule = openapi_client.models.transition_rule.TransitionRule(
                    id = '0', 
                    name = '0', 
                    label = '', 
                    description = '', 
                    text = '', 
                    instance_type = 'TransitionRule', ),
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
                instance_type = 'Encounter'
            )
        else:
            return EncounterInput(
                id = '0',
                name = '0',
                type = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                instance_type = 'Encounter',
        )
        """

    def testEncounterInput(self):
        """Test EncounterInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
