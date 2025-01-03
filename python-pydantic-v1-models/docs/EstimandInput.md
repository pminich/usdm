# EstimandInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**population_summary** | **str** |  | 
**analysis_population_id** | **str** |  | 
**intervention_ids** | **List[str]** |  | 
**variable_of_interest_id** | **str** |  | 
**intercurrent_events** | [**List[IntercurrentEventInput]**](IntercurrentEventInput.md) |  | 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.estimand_input import EstimandInput

# TODO update the JSON string below
json = "{}"
# create an instance of EstimandInput from a JSON string
estimand_input_instance = EstimandInput.from_json(json)
# print the JSON string representation of the object
print EstimandInput.to_json()

# convert the object into a dict
estimand_input_dict = estimand_input_instance.to_dict()
# create an instance of EstimandInput from a dict
estimand_input_from_dict = EstimandInput.from_dict(estimand_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


