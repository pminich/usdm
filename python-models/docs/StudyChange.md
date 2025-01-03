# StudyChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**summary** | **str** |  | 
**rationale** | **str** |  | 
**changed_sections** | [**List[DocumentContentReference]**](DocumentContentReference.md) |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_change import StudyChange

# TODO update the JSON string below
json = "{}"
# create an instance of StudyChange from a JSON string
study_change_instance = StudyChange.from_json(json)
# print the JSON string representation of the object
print(StudyChange.to_json())

# convert the object into a dict
study_change_dict = study_change_instance.to_dict()
# create an instance of StudyChange from a dict
study_change_from_dict = StudyChange.from_dict(study_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


