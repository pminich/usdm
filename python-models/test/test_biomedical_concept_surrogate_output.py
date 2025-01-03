# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.biomedical_concept_surrogate_output import BiomedicalConceptSurrogateOutput

class TestBiomedicalConceptSurrogateOutput(unittest.TestCase):
    """BiomedicalConceptSurrogateOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BiomedicalConceptSurrogateOutput:
        """Test BiomedicalConceptSurrogateOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BiomedicalConceptSurrogateOutput`
        """
        model = BiomedicalConceptSurrogateOutput()
        if include_optional:
            return BiomedicalConceptSurrogateOutput(
                id = '0',
                name = '0',
                label = '',
                description = '',
                reference = '',
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
                instance_type = 'BiomedicalConceptSurrogate'
            )
        else:
            return BiomedicalConceptSurrogateOutput(
                id = '0',
                name = '0',
                instance_type = 'BiomedicalConceptSurrogate',
        )
        """

    def testBiomedicalConceptSurrogateOutput(self):
        """Test BiomedicalConceptSurrogateOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
