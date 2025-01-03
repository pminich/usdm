# StudyOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**versions** | [**List[StudyVersionOutput]**](StudyVersionOutput.md) |  | [optional] [default to []]
**documented_by** | [**List[StudyDefinitionDocumentOutput]**](StudyDefinitionDocumentOutput.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_output import StudyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyOutput from a JSON string
study_output_instance = StudyOutput.from_json(json)
# print the JSON string representation of the object
print(StudyOutput.to_json())

# convert the object into a dict
study_output_dict = study_output_instance.to_dict()
# create an instance of StudyOutput from a dict
study_output_from_dict = StudyOutput.from_dict(study_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


