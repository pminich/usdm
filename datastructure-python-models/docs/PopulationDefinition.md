# PopulationDefinition

NCI C-Code: C207593 Definition: A concise explanation of the meaning of a population. Preferred Term: Population Definition

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

## Example

```python
from openapi_client.models.population_definition import PopulationDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PopulationDefinition from a JSON string
population_definition_instance = PopulationDefinition.from_json(json)
# print the JSON string representation of the object
print(PopulationDefinition.to_json())

# convert the object into a dict
population_definition_dict = population_definition_instance.to_dict()
# create an instance of PopulationDefinition from a dict
population_definition_from_dict = PopulationDefinition.from_dict(population_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


