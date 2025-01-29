# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.observational_study_design import ObservationalStudyDesign

class TestObservationalStudyDesign(unittest.TestCase):
    """ObservationalStudyDesign unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationalStudyDesign:
        """Test ObservationalStudyDesign
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationalStudyDesign`
        """
        model = ObservationalStudyDesign()
        if include_optional:
            return ObservationalStudyDesign(
                id = '',
                name = '',
                description = '',
                label = '',
                rationale = '',
                activities = [
                    ''
                    ],
                study_phase = '',
                biospecimen_retentions = [
                    ''
                    ],
                study_type = '',
                therapeutic_areas = [
                    ''
                    ],
                characteristics = [
                    ''
                    ],
                notes = [
                    ''
                    ],
                encounters = [
                    ''
                    ],
                estimands = [
                    ''
                    ],
                indications = [
                    ''
                    ],
                objectives = [
                    ''
                    ],
                schedule_timelines = [
                    ''
                    ],
                arms = [
                    ''
                    ],
                study_cells = [
                    ''
                    ],
                document_versions = [
                    ''
                    ],
                elements = [
                    ''
                    ],
                study_interventions = [
                    ''
                    ],
                epochs = [
                    ''
                    ],
                population = '',
                time_perspective = '',
                sub_types = [
                    ''
                    ],
                model = '',
                sampling_method = '',
                biomedical_concepts = [
                    ''
                    ],
                bc_categories = [
                    ''
                    ],
                bc_surrogates = [
                    ''
                    ],
                analysis_populations = [
                    ''
                    ],
                dictionaries = [
                    ''
                    ],
                conditions = [
                    ''
                    ],
                instance_type = ''
            )
        else:
            return ObservationalStudyDesign(
                id = '',
                name = '',
                description = '',
                label = '',
                rationale = '',
                arms = [
                    ''
                    ],
                study_cells = [
                    ''
                    ],
                epochs = [
                    ''
                    ],
                time_perspective = '',
                model = '',
        )
        """

    def testObservationalStudyDesign(self):
        """Test ObservationalStudyDesign"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
