# StudyVersionInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version_identifier** | **str** |  | 
**rationale** | **str** |  | 
**document_version_ids** | **List[str]** |  | [optional] [default to []]
**date_values** | [**List[GovernanceDateInput]**](GovernanceDateInput.md) |  | [optional] [default to []]
**amendments** | [**List[StudyAmendmentInput]**](StudyAmendmentInput.md) |  | [optional] [default to []]
**business_therapeutic_areas** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**study_identifiers** | [**List[StudyIdentifier]**](StudyIdentifier.md) |  | 
**reference_identifiers** | [**List[ReferenceIdentifier]**](ReferenceIdentifier.md) |  | [optional] [default to []]
**study_designs** | [**List[StudyVersionInputStudyDesignsInner]**](StudyVersionInputStudyDesignsInner.md) |  | [optional] [default to []]
**titles** | [**List[StudyTitle]**](StudyTitle.md) |  | 
**criteria** | [**List[EligibilityCriterionInput]**](EligibilityCriterionInput.md) |  | 
**narrative_content_items** | [**List[NarrativeContentItem]**](NarrativeContentItem.md) |  | [optional] [default to []]
**abbreviations** | [**List[AbbreviationInput]**](AbbreviationInput.md) |  | [optional] [default to []]
**roles** | [**List[StudyRole]**](StudyRole.md) |  | [optional] [default to []]
**organizations** | [**List[OrganizationInput]**](OrganizationInput.md) |  | [optional] [default to []]
**administrable_products** | [**List[AdministrableProductInput]**](AdministrableProductInput.md) |  | [optional] [default to []]
**medical_devices** | [**List[MedicalDeviceInput]**](MedicalDeviceInput.md) |  | [optional] [default to []]
**product_organization_roles** | [**List[ProductOrganizationRole]**](ProductOrganizationRole.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_version_input import StudyVersionInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyVersionInput from a JSON string
study_version_input_instance = StudyVersionInput.from_json(json)
# print the JSON string representation of the object
print StudyVersionInput.to_json()

# convert the object into a dict
study_version_input_dict = study_version_input_instance.to_dict()
# create an instance of StudyVersionInput from a dict
study_version_input_from_dict = StudyVersionInput.from_dict(study_version_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


