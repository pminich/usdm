# EstimandOutput


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
**intercurrent_events** | [**List[IntercurrentEventOutput]**](IntercurrentEventOutput.md) |  | 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.estimand_output import EstimandOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EstimandOutput from a JSON string
estimand_output_instance = EstimandOutput.from_json(json)
# print the JSON string representation of the object
print EstimandOutput.to_json()

# convert the object into a dict
estimand_output_dict = estimand_output_instance.to_dict()
# create an instance of EstimandOutput from a dict
estimand_output_from_dict = EstimandOutput.from_dict(estimand_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


