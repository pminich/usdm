# StudyVersion

NCI C-Code: C188816 Definition: A plan at a particular point in time for a study. Preferred Term: Study Version

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version_identifier** | **str** |  | 
**rationale** | **str** |  | 
**abbreviations** | **List[str]** |  | [optional] 
**business_therapeutic_areas** | **List[str]** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**date_values** | **List[str]** |  | [optional] 
**reference_identifiers** | **List[str]** |  | [optional] 
**amendments** | **List[str]** |  | [optional] 
**document_versions** | **List[str]** |  | [optional] 
**study_designs** | **List[str]** |  | [optional] 
**study_identifiers** | **List[str]** |  | 
**titles** | **List[str]** |  | 
**criteria** | **List[str]** |  | [optional] 
**narrative_content_items** | **List[str]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**organizations** | **List[str]** |  | [optional] 
**administrable_products** | **List[str]** |  | [optional] 
**medical_devices** | **List[str]** |  | [optional] 
**product_organization_roles** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_version import StudyVersion

# TODO update the JSON string below
json = "{}"
# create an instance of StudyVersion from a JSON string
study_version_instance = StudyVersion.from_json(json)
# print the JSON string representation of the object
print StudyVersion.to_json()

# convert the object into a dict
study_version_dict = study_version_instance.to_dict()
# create an instance of StudyVersion from a dict
study_version_from_dict = StudyVersion.from_dict(study_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


