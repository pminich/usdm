# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.objective_output import ObjectiveOutput

class TestObjectiveOutput(unittest.TestCase):
    """ObjectiveOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectiveOutput:
        """Test ObjectiveOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectiveOutput`
        """
        model = ObjectiveOutput()
        if include_optional:
            return ObjectiveOutput(
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
                instance_type = 'Objective',
                level = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                endpoints = [
                    openapi_client.models.endpoint.Endpoint(
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
                        instance_type = 'Endpoint', 
                        purpose = '', 
                        level = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), )
                    ]
            )
        else:
            return ObjectiveOutput(
                id = '0',
                name = '0',
                text = '',
                instance_type = 'Objective',
                level = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
        )
        """

    def testObjectiveOutput(self):
        """Test ObjectiveOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
