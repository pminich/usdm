# StudyDesignPopulationOutput


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
**cohorts** | [**List[StudyCohortOutput]**](StudyCohortOutput.md) |  | [optional] [default to []]

## Example

```python
from openapi_client.models.study_design_population_output import StudyDesignPopulationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyDesignPopulationOutput from a JSON string
study_design_population_output_instance = StudyDesignPopulationOutput.from_json(json)
# print the JSON string representation of the object
print(StudyDesignPopulationOutput.to_json())

# convert the object into a dict
study_design_population_output_dict = study_design_population_output_instance.to_dict()
# create an instance of StudyDesignPopulationOutput from a dict
study_design_population_output_from_dict = StudyDesignPopulationOutput.from_dict(study_design_population_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


