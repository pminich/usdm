# StudyArmOutput


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
from openapi_client.models.study_arm_output import StudyArmOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyArmOutput from a JSON string
study_arm_output_instance = StudyArmOutput.from_json(json)
# print the JSON string representation of the object
print StudyArmOutput.to_json()

# convert the object into a dict
study_arm_output_dict = study_arm_output_instance.to_dict()
# create an instance of StudyArmOutput from a dict
study_arm_output_from_dict = StudyArmOutput.from_dict(study_arm_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


