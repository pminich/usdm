# StudyCohortOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**includes_healthy_subjects** | **bool** |  | 
**planned_enrollment_number** | [**RangeOutput**](RangeOutput.md) |  | [optional] 
**planned_completion_number** | [**RangeOutput**](RangeOutput.md) |  | [optional] 
**planned_sex** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**criterion_ids** | **List[str]** |  | [optional] [default to []]
**planned_age** | [**RangeOutput**](RangeOutput.md) |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 
**characteristics** | [**List[CharacteristicOutput]**](CharacteristicOutput.md) |  | [optional] [default to []]

## Example

```python
from openapi_client.models.study_cohort_output import StudyCohortOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyCohortOutput from a JSON string
study_cohort_output_instance = StudyCohortOutput.from_json(json)
# print the JSON string representation of the object
print(StudyCohortOutput.to_json())

# convert the object into a dict
study_cohort_output_dict = study_cohort_output_instance.to_dict()
# create an instance of StudyCohortOutput from a dict
study_cohort_output_from_dict = StudyCohortOutput.from_dict(study_cohort_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


