# StudyRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**code** | [**Code**](Code.md) |  | 
**applies_to_ids** | **List[str]** |  | [optional] [default to []]
**assigned_persons** | [**List[AssignedPerson]**](AssignedPerson.md) |  | [optional] [default to []]
**organization_ids** | **List[str]** |  | [optional] [default to []]
**masking** | [**Masking**](Masking.md) |  | [optional] 
**instance_type** | **str** |  | 

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


