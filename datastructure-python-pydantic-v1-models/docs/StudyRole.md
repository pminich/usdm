# StudyRole

NCI C-Code: CNEW Definition: A designation that identifies the function of study personnel or an organization within the context of the study. Preferred Term: Study Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**description** | **str** |  | 
**assigned_persons** | **List[str]** |  | [optional] 
**code** | **str** |  | 
**masking** | **str** |  | [optional] 
**organizations** | **List[str]** |  | [optional] 
**applies_to** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_role import StudyRole

# TODO update the JSON string below
json = "{}"
# create an instance of StudyRole from a JSON string
study_role_instance = StudyRole.from_json(json)
# print the JSON string representation of the object
print StudyRole.to_json()

# convert the object into a dict
study_role_dict = study_role_instance.to_dict()
# create an instance of StudyRole from a dict
study_role_from_dict = StudyRole.from_dict(study_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


