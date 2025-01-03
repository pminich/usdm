# EligibilityCriterionOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**text** | **str** |  | 
**dictionary_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 
**category** | [**Code**](Code.md) |  | 
**identifier** | **str** |  | 
**next_id** | **str** |  | [optional] 
**previous_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.eligibility_criterion_output import EligibilityCriterionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityCriterionOutput from a JSON string
eligibility_criterion_output_instance = EligibilityCriterionOutput.from_json(json)
# print the JSON string representation of the object
print EligibilityCriterionOutput.to_json()

# convert the object into a dict
eligibility_criterion_output_dict = eligibility_criterion_output_instance.to_dict()
# create an instance of EligibilityCriterionOutput from a dict
eligibility_criterion_output_from_dict = EligibilityCriterionOutput.from_dict(eligibility_criterion_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


