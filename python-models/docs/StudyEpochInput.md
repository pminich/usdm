# StudyEpochInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**Code**](Code.md) |  | 
**previous_id** | **str** |  | [optional] 
**next_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_epoch_input import StudyEpochInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyEpochInput from a JSON string
study_epoch_input_instance = StudyEpochInput.from_json(json)
# print the JSON string representation of the object
print(StudyEpochInput.to_json())

# convert the object into a dict
study_epoch_input_dict = study_epoch_input_instance.to_dict()
# create an instance of StudyEpochInput from a dict
study_epoch_input_from_dict = StudyEpochInput.from_dict(study_epoch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


