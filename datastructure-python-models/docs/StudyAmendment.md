# StudyAmendment

NCI C-Code: C207594 Definition: A written description of a change(s) to, or formal clarification of, a study. Preferred Term: Study Amendment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**number** | **str** |  | 
**summary** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**geographic_scopes** | **List[str]** |  | 
**date_values** | **List[str]** |  | [optional] 
**impacts** | **List[str]** |  | [optional] 
**enrollments** | **List[str]** |  | [optional] 
**secondary_reasons** | **List[str]** |  | [optional] 
**changes** | **List[str]** |  | 
**previous** | **str** |  | [optional] 
**primary_reason** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_amendment import StudyAmendment

# TODO update the JSON string below
json = "{}"
# create an instance of StudyAmendment from a JSON string
study_amendment_instance = StudyAmendment.from_json(json)
# print the JSON string representation of the object
print(StudyAmendment.to_json())

# convert the object into a dict
study_amendment_dict = study_amendment_instance.to_dict()
# create an instance of StudyAmendment from a dict
study_amendment_from_dict = StudyAmendment.from_dict(study_amendment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


