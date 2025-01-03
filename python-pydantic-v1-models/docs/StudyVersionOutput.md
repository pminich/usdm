# StudyVersionOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version_identifier** | **str** |  | 
**rationale** | **str** |  | 
**document_version_ids** | **List[str]** |  | [optional] [default to []]
**date_values** | [**List[GovernanceDateOutput]**](GovernanceDateOutput.md) |  | [optional] [default to []]
**amendments** | [**List[StudyAmendmentOutput]**](StudyAmendmentOutput.md) |  | [optional] [default to []]
**business_therapeutic_areas** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**study_identifiers** | [**List[StudyIdentifier]**](StudyIdentifier.md) |  | 
**reference_identifiers** | [**List[ReferenceIdentifier]**](ReferenceIdentifier.md) |  | [optional] [default to []]
**study_designs** | [**List[SearchStudyDesignV3StudyDesignsGet200ResponseInner]**](SearchStudyDesignV3StudyDesignsGet200ResponseInner.md) |  | [optional] [default to []]
**titles** | [**List[StudyTitle]**](StudyTitle.md) |  | 
**criteria** | [**List[EligibilityCriterionOutput]**](EligibilityCriterionOutput.md) |  | 
**narrative_content_items** | [**List[NarrativeContentItem]**](NarrativeContentItem.md) |  | [optional] [default to []]
**abbreviations** | [**List[AbbreviationOutput]**](AbbreviationOutput.md) |  | [optional] [default to []]
**roles** | [**List[StudyRole]**](StudyRole.md) |  | [optional] [default to []]
**organizations** | [**List[OrganizationOutput]**](OrganizationOutput.md) |  | [optional] [default to []]
**administrable_products** | [**List[AdministrableProductOutput]**](AdministrableProductOutput.md) |  | [optional] [default to []]
**medical_devices** | [**List[MedicalDeviceOutput]**](MedicalDeviceOutput.md) |  | [optional] [default to []]
**product_organization_roles** | [**List[ProductOrganizationRole]**](ProductOrganizationRole.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_version_output import StudyVersionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyVersionOutput from a JSON string
study_version_output_instance = StudyVersionOutput.from_json(json)
# print the JSON string representation of the object
print StudyVersionOutput.to_json()

# convert the object into a dict
study_version_output_dict = study_version_output_instance.to_dict()
# create an instance of StudyVersionOutput from a dict
study_version_output_from_dict = StudyVersionOutput.from_dict(study_version_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


