# StudyCohort

NCI C-Code: C61512 Definition: A group of individuals who share a set of characteristics (e.g., exposures, experiences, attributes), which logically defines a population under study. Preferred Term: Study Cohort

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**includes_healthy_subjects** | **str** |  | 
**planned_sex** | **str** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**criteria** | **List[str]** |  | [optional] 
**planned_age** | **str** |  | [optional] 
**planned_enrollment_number** | **str** |  | [optional] 
**planned_completion_number** | **str** |  | [optional] 
**characteristics** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_cohort import StudyCohort

# TODO update the JSON string below
json = "{}"
# create an instance of StudyCohort from a JSON string
study_cohort_instance = StudyCohort.from_json(json)
# print the JSON string representation of the object
print(StudyCohort.to_json())

# convert the object into a dict
study_cohort_dict = study_cohort_instance.to_dict()
# create an instance of StudyCohort from a dict
study_cohort_from_dict = StudyCohort.from_dict(study_cohort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


