# StudyArm

NCI C-Code: C174447 Definition: A planned pathway assigned to the subject as they progress through the study, usually referred to by a name that reflects one or more treatments, exposures, and/or controls included in the path. Preferred Term: Study Arm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**data_origin_description** | **str** |  | 
**data_origin_type** | **str** |  | 
**type** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**populations** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_arm import StudyArm

# TODO update the JSON string below
json = "{}"
# create an instance of StudyArm from a JSON string
study_arm_instance = StudyArm.from_json(json)
# print the JSON string representation of the object
print StudyArm.to_json()

# convert the object into a dict
study_arm_dict = study_arm_instance.to_dict()
# create an instance of StudyArm from a dict
study_arm_from_dict = StudyArm.from_dict(study_arm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


