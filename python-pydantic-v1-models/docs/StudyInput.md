# StudyInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**versions** | [**List[StudyVersionInput]**](StudyVersionInput.md) |  | [optional] [default to []]
**documented_by** | [**List[StudyDefinitionDocumentInput]**](StudyDefinitionDocumentInput.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_input import StudyInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyInput from a JSON string
study_input_instance = StudyInput.from_json(json)
# print the JSON string representation of the object
print StudyInput.to_json()

# convert the object into a dict
study_input_dict = study_input_instance.to_dict()
# create an instance of StudyInput from a dict
study_input_from_dict = StudyInput.from_dict(study_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


