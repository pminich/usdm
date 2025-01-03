# StudyEpochOutput


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
from openapi_client.models.study_epoch_output import StudyEpochOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyEpochOutput from a JSON string
study_epoch_output_instance = StudyEpochOutput.from_json(json)
# print the JSON string representation of the object
print(StudyEpochOutput.to_json())

# convert the object into a dict
study_epoch_output_dict = study_epoch_output_instance.to_dict()
# create an instance of StudyEpochOutput from a dict
study_epoch_output_from_dict = StudyEpochOutput.from_dict(study_epoch_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


