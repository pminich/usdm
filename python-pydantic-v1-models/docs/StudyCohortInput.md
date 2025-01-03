# StudyCohortInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**includes_healthy_subjects** | **bool** |  | 
**planned_enrollment_number** | [**RangeInput**](RangeInput.md) |  | [optional] 
**planned_completion_number** | [**RangeInput**](RangeInput.md) |  | [optional] 
**planned_sex** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**criterion_ids** | **List[str]** |  | [optional] [default to []]
**planned_age** | [**RangeInput**](RangeInput.md) |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 
**characteristics** | [**List[CharacteristicInput]**](CharacteristicInput.md) |  | [optional] [default to []]

## Example

```python
from openapi_client.models.study_cohort_input import StudyCohortInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyCohortInput from a JSON string
study_cohort_input_instance = StudyCohortInput.from_json(json)
# print the JSON string representation of the object
print StudyCohortInput.to_json()

# convert the object into a dict
study_cohort_input_dict = study_cohort_input_instance.to_dict()
# create an instance of StudyCohortInput from a dict
study_cohort_input_from_dict = StudyCohortInput.from_dict(study_cohort_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


