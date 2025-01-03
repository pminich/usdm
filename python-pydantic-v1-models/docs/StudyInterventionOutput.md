# StudyInterventionOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**role** | [**Code**](Code.md) |  | 
**type** | [**Code**](Code.md) |  | 
**minimum_response_duration** | [**QuantityOutput**](QuantityOutput.md) |  | [optional] 
**codes** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**administrations** | [**List[AdministrationOutput]**](AdministrationOutput.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_intervention_output import StudyInterventionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyInterventionOutput from a JSON string
study_intervention_output_instance = StudyInterventionOutput.from_json(json)
# print the JSON string representation of the object
print StudyInterventionOutput.to_json()

# convert the object into a dict
study_intervention_output_dict = study_intervention_output_instance.to_dict()
# create an instance of StudyInterventionOutput from a dict
study_intervention_output_from_dict = StudyInterventionOutput.from_dict(study_intervention_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


