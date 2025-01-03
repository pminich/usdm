# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ingredient_output import IngredientOutput

class TestIngredientOutput(unittest.TestCase):
    """IngredientOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IngredientOutput:
        """Test IngredientOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IngredientOutput`
        """
        model = IngredientOutput()
        if include_optional:
            return IngredientOutput(
                id = '0',
                role = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                substance = openapi_client.models.substance.Substance(
                    id = '0', 
                    name = '0', 
                    label = '', 
                    description = '', 
                    codes = [
                        openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', )
                        ], 
                    strengths = [
                        openapi_client.models.strength.Strength(
                            id = '0', 
                            name = '0', 
                            label = '', 
                            description = '', 
                            denominator = openapi_client.models.quantity.Quantity(
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
                                        
                                        ], 
                                    instance_type = 'AliasCode', ), 
                                instance_type = 'Quantity', ), 
                            numerator = null, 
                            instance_type = 'Strength', )
                        ], 
                    reference_substance = openapi_client.models.substance.Substance(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        strengths = [
                            openapi_client.models.strength.Strength(
                                id = '0', 
                                name = '0', 
                                label = '', 
                                description = '', 
                                instance_type = 'Strength', )
                            ], 
                        instance_type = 'Substance', ), 
                    instance_type = 'Substance', ),
                instance_type = 'Ingredient'
            )
        else:
            return IngredientOutput(
                id = '0',
                role = openapi_client.models.code.Code(
                    id = '0', 
                    code = '', 
                    code_system = '', 
                    code_system_version = '', 
                    decode = '', 
                    instance_type = 'Code', ),
                substance = openapi_client.models.substance.Substance(
                    id = '0', 
                    name = '0', 
                    label = '', 
                    description = '', 
                    codes = [
                        openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', )
                        ], 
                    strengths = [
                        openapi_client.models.strength.Strength(
                            id = '0', 
                            name = '0', 
                            label = '', 
                            description = '', 
                            denominator = openapi_client.models.quantity.Quantity(
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
                                        
                                        ], 
                                    instance_type = 'AliasCode', ), 
                                instance_type = 'Quantity', ), 
                            numerator = null, 
                            instance_type = 'Strength', )
                        ], 
                    reference_substance = openapi_client.models.substance.Substance(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        strengths = [
                            openapi_client.models.strength.Strength(
                                id = '0', 
                                name = '0', 
                                label = '', 
                                description = '', 
                                instance_type = 'Strength', )
                            ], 
                        instance_type = 'Substance', ), 
                    instance_type = 'Substance', ),
                instance_type = 'Ingredient',
        )
        """

    def testIngredientOutput(self):
        """Test IngredientOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
