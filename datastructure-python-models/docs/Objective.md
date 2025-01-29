# Objective

NCI C-Code: C142450 Definition: The reason for performing a study in terms of the scientific questions to be answered by the analysis of data collected during the study. Preferred Term: Study Objective

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**text** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**dictionary** | **str** |  | [optional] 
**level** | **str** |  | 
**endpoints** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.objective import Objective

# TODO update the JSON string below
json = "{}"
# create an instance of Objective from a JSON string
objective_instance = Objective.from_json(json)
# print the JSON string representation of the object
print(Objective.to_json())

# convert the object into a dict
objective_dict = objective_instance.to_dict()
# create an instance of Objective from a dict
objective_from_dict = Objective.from_dict(objective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


