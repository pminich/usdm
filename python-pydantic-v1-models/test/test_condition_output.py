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

from openapi_client.models.condition_output import ConditionOutput  # noqa: E501

class TestConditionOutput(unittest.TestCase):
    """ConditionOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConditionOutput:
        """Test ConditionOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConditionOutput`
        """
        model = ConditionOutput()  # noqa: E501
        if include_optional:
            return ConditionOutput(
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
                instance_type = 'Condition',
                context_ids = [
                    ''
                    ],
                applies_to_ids = [
                    ''
                    ]
            )
        else:
            return ConditionOutput(
                id = '0',
                name = '0',
                text = '',
                instance_type = 'Condition',
        )
        """

    def testConditionOutput(self):
        """Test ConditionOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
