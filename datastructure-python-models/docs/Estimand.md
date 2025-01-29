# Estimand

NCI C-Code: C188813 Definition: A precise description of the treatment effect reflecting the clinical question posed by a given clinical trial objective. It summarises at a population level what the outcomes would be in the same patients under different treatment conditions being compared. (ICH E9 R1 Addendum) Preferred Term: Estimand

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**population_summary** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**analysis_population** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**variable_of_interest** | **str** |  | 
**intercurrent_events** | **List[str]** |  | 
**interventions** | **List[str]** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.estimand import Estimand

# TODO update the JSON string below
json = "{}"
# create an instance of Estimand from a JSON string
estimand_instance = Estimand.from_json(json)
# print the JSON string representation of the object
print(Estimand.to_json())

# convert the object into a dict
estimand_dict = estimand_instance.to_dict()
# create an instance of Estimand from a dict
estimand_from_dict = Estimand.from_dict(estimand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


