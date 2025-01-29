# StudyDesignPopulation

NCI C-Code: C142728 Definition: The population within the general population to which the study results can be generalized. Preferred Term: Study Design Population

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
**cohorts** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_design_population import StudyDesignPopulation

# TODO update the JSON string below
json = "{}"
# create an instance of StudyDesignPopulation from a JSON string
study_design_population_instance = StudyDesignPopulation.from_json(json)
# print the JSON string representation of the object
print StudyDesignPopulation.to_json()

# convert the object into a dict
study_design_population_dict = study_design_population_instance.to_dict()
# create an instance of StudyDesignPopulation from a dict
study_design_population_from_dict = StudyDesignPopulation.from_dict(study_design_population_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


