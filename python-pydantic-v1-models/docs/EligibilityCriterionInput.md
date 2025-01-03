# EligibilityCriterionInput


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
from openapi_client.models.eligibility_criterion_input import EligibilityCriterionInput

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityCriterionInput from a JSON string
eligibility_criterion_input_instance = EligibilityCriterionInput.from_json(json)
# print the JSON string representation of the object
print EligibilityCriterionInput.to_json()

# convert the object into a dict
eligibility_criterion_input_dict = eligibility_criterion_input_instance.to_dict()
# create an instance of EligibilityCriterionInput from a dict
eligibility_criterion_input_from_dict = EligibilityCriterionInput.from_dict(eligibility_criterion_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


