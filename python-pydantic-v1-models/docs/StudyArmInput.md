# StudyArmInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**Code**](Code.md) |  | 
**data_origin_description** | **str** |  | 
**data_origin_type** | [**Code**](Code.md) |  | 
**population_ids** | **List[str]** |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_arm_input import StudyArmInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyArmInput from a JSON string
study_arm_input_instance = StudyArmInput.from_json(json)
# print the JSON string representation of the object
print StudyArmInput.to_json()

# convert the object into a dict
study_arm_input_dict = study_arm_input_instance.to_dict()
# create an instance of StudyArmInput from a dict
study_arm_input_from_dict = StudyArmInput.from_dict(study_arm_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


