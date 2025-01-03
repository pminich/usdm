# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.study_version_input import StudyVersionInput

class TestStudyVersionInput(unittest.TestCase):
    """StudyVersionInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudyVersionInput:
        """Test StudyVersionInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudyVersionInput`
        """
        model = StudyVersionInput()
        if include_optional:
            return StudyVersionInput(
                id = '0',
                version_identifier = '',
                rationale = '',
                document_version_ids = [
                    ''
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
                amendments = [
                    openapi_client.models.study_amendment.StudyAmendment(
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
                                type = , 
                                text = '', 
                                is_substantial = True, 
                                notes = [
                                    openapi_client.models.comment_annotation.CommentAnnotation(
                                        id = '0', 
                                        text = '', 
                                        codes = [
                                            
                                            ], 
                                        instance_type = 'CommentAnnotation', )
                                    ], 
                                instance_type = 'StudyAmendmentImpact', )
                            ], 
                        geographic_scopes = [
                            openapi_client.models.geographic_scope.GeographicScope(
                                id = '0', 
                                type = , 
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
                                        standard_code = , 
                                        standard_code_aliases = [
                                            
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
                                type = , 
                                date_value = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                geographic_scopes = [
                                    
                                    ], 
                                instance_type = 'GovernanceDate', )
                            ], 
                        previous_id = '', 
                        notes = [
                            openapi_client.models.comment_annotation.CommentAnnotation(
                                id = '0', 
                                text = '', 
                                instance_type = 'CommentAnnotation', )
                            ], 
                        instance_type = 'StudyAmendment', )
                    ],
                business_therapeutic_areas = [
                    openapi_client.models.code.Code(
                        id = '0', 
                        code = '', 
                        code_system = '', 
                        code_system_version = '', 
                        decode = '', 
                        instance_type = 'Code', )
                    ],
                study_identifiers = [
                    openapi_client.models.study_identifier.StudyIdentifier(
                        id = '0', 
                        text = '', 
                        scope_id = '', 
                        instance_type = 'StudyIdentifier', )
                    ],
                reference_identifiers = [
                    openapi_client.models.reference_identifier.ReferenceIdentifier(
                        id = '0', 
                        text = '', 
                        scope_id = '', 
                        instance_type = 'ReferenceIdentifier', 
                        type = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), )
                    ],
                study_designs = [
                    null
                    ],
                titles = [
                    openapi_client.models.study_title.StudyTitle(
                        id = '0', 
                        text = '', 
                        type = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        instance_type = 'StudyTitle', )
                    ],
                criteria = [
                    openapi_client.models.eligibility_criterion.EligibilityCriterion(
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
                        instance_type = 'EligibilityCriterion', 
                        category = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        identifier = '', 
                        next_id = '', 
                        previous_id = '', )
                    ],
                narrative_content_items = [
                    openapi_client.models.narrative_content_item.NarrativeContentItem(
                        id = '0', 
                        name = '0', 
                        text = '', 
                        instance_type = 'NarrativeContentItem', )
                    ],
                abbreviations = [
                    openapi_client.models.abbreviation.Abbreviation(
                        id = '0', 
                        abbreviated_text = '0', 
                        expanded_text = '0', 
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
                        instance_type = 'Abbreviation', )
                    ],
                roles = [
                    openapi_client.models.study_role.StudyRole(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        code = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        applies_to_ids = [
                            ''
                            ], 
                        assigned_persons = [
                            openapi_client.models.assigned_person.AssignedPerson(
                                id = '0', 
                                name = '0', 
                                label = '', 
                                description = '', 
                                job_title = '', 
                                organization_id = '', 
                                instance_type = 'AssignedPerson', )
                            ], 
                        organization_ids = [
                            ''
                            ], 
                        masking = openapi_client.models.masking.Masking(
                            id = '0', 
                            description = '', 
                            instance_type = 'Masking', ), 
                        instance_type = 'StudyRole', )
                    ],
                organizations = [
                    openapi_client.models.organization.Organization(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        type = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        identifier_scheme = '', 
                        identifier = '', 
                        legal_address = openapi_client.models.address.Address(
                            id = '0', 
                            text = '', 
                            lines = [
                                ''
                                ], 
                            city = '', 
                            district = '', 
                            state = '', 
                            postal_code = '', 
                            country = openapi_client.models.code.Code(
                                id = '0', 
                                code = '', 
                                code_system = '', 
                                code_system_version = '', 
                                decode = '', 
                                instance_type = 'Code', ), 
                            instance_type = 'Address', ), 
                        managed_sites = [
                            openapi_client.models.study_site.StudySite(
                                id = '0', 
                                name = '0', 
                                label = '', 
                                description = '', 
                                country = , 
                                instance_type = 'StudySite', )
                            ], 
                        instance_type = 'Organization', )
                    ],
                administrable_products = [
                    openapi_client.models.administrable_product.AdministrableProduct(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        pharmacologic_class = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        administrable_dose_form = openapi_client.models.alias_code.AliasCode(
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
                        product_designation = , 
                        sourcing = , 
                        properties = [
                            openapi_client.models.administrable_product_property.AdministrableProductProperty(
                                id = '0', 
                                name = '0', 
                                text = '', 
                                type = , 
                                quantity = openapi_client.models.quantity.Quantity(
                                    id = '0', 
                                    value = 1.337, 
                                    unit = openapi_client.models.alias_code.AliasCode(
                                        id = '0', 
                                        standard_code = , 
                                        instance_type = 'AliasCode', ), 
                                    instance_type = 'Quantity', ), 
                                instance_type = 'AdministrableProductProperty', )
                            ], 
                        identifiers = [
                            openapi_client.models.administrable_product_identifier.AdministrableProductIdentifier(
                                id = '0', 
                                text = '', 
                                scope_id = '', 
                                instance_type = 'AdministrableProductIdentifier', )
                            ], 
                        ingredients = [
                            openapi_client.models.ingredient.Ingredient(
                                id = '0', 
                                role = , 
                                substance = openapi_client.models.substance.Substance(
                                    id = '0', 
                                    name = '0', 
                                    label = '', 
                                    description = '', 
                                    codes = [
                                        
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
                                instance_type = 'Ingredient', )
                            ], 
                        notes = [
                            openapi_client.models.comment_annotation.CommentAnnotation(
                                id = '0', 
                                text = '', 
                                instance_type = 'CommentAnnotation', )
                            ], 
                        instance_type = 'AdministrableProduct', )
                    ],
                medical_devices = [
                    openapi_client.models.medical_device.MedicalDevice(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        hardware_version = '', 
                        software_version = '', 
                        embedded_product_id = '', 
                        sourcing = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        identifiers = [
                            openapi_client.models.medical_device_identifier.MedicalDeviceIdentifier(
                                id = '0', 
                                text = '', 
                                scope_id = '', 
                                instance_type = 'MedicalDeviceIdentifier', 
                                type = openapi_client.models.code.Code(
                                    id = '0', 
                                    code = '', 
                                    code_system = '', 
                                    code_system_version = '', 
                                    decode = '', 
                                    instance_type = 'Code', ), )
                            ], 
                        notes = [
                            openapi_client.models.comment_annotation.CommentAnnotation(
                                id = '0', 
                                text = '', 
                                codes = [
                                    
                                    ], 
                                instance_type = 'CommentAnnotation', )
                            ], 
                        instance_type = 'MedicalDevice', )
                    ],
                product_organization_roles = [
                    openapi_client.models.product_organization_role.ProductOrganizationRole(
                        id = '0', 
                        name = '0', 
                        label = '', 
                        description = '', 
                        code = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        applies_to_ids = [
                            ''
                            ], 
                        organization_id = '', 
                        instance_type = 'ProductOrganizationRole', )
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
                instance_type = 'StudyVersion'
            )
        else:
            return StudyVersionInput(
                id = '0',
                version_identifier = '',
                rationale = '',
                study_identifiers = [
                    openapi_client.models.study_identifier.StudyIdentifier(
                        id = '0', 
                        text = '', 
                        scope_id = '', 
                        instance_type = 'StudyIdentifier', )
                    ],
                titles = [
                    openapi_client.models.study_title.StudyTitle(
                        id = '0', 
                        text = '', 
                        type = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        instance_type = 'StudyTitle', )
                    ],
                criteria = [
                    openapi_client.models.eligibility_criterion.EligibilityCriterion(
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
                        instance_type = 'EligibilityCriterion', 
                        category = openapi_client.models.code.Code(
                            id = '0', 
                            code = '', 
                            code_system = '', 
                            code_system_version = '', 
                            decode = '', 
                            instance_type = 'Code', ), 
                        identifier = '', 
                        next_id = '', 
                        previous_id = '', )
                    ],
                instance_type = 'StudyVersion',
        )
        """

    def testStudyVersionInput(self):
        """Test StudyVersionInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
