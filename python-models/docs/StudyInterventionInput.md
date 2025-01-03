# StudyInterventionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**role** | [**Code**](Code.md) |  | 
**type** | [**Code**](Code.md) |  | 
**minimum_response_duration** | [**QuantityInput**](QuantityInput.md) |  | [optional] 
**codes** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**administrations** | [**List[AdministrationInput]**](AdministrationInput.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_intervention_input import StudyInterventionInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyInterventionInput from a JSON string
study_intervention_input_instance = StudyInterventionInput.from_json(json)
# print the JSON string representation of the object
print(StudyInterventionInput.to_json())

# convert the object into a dict
study_intervention_input_dict = study_intervention_input_instance.to_dict()
# create an instance of StudyInterventionInput from a dict
study_intervention_input_from_dict = StudyInterventionInput.from_dict(study_intervention_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


