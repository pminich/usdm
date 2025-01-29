# EligibilityCriterion

NCI C-Code: C16112 Definition: Characteristics which are necessary to allow a subject to participate in a clinical study, as outlined in the study protocol. The concept covers inclusion and exclusion criteria. Preferred Term: Study Eligibility Criterion

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
**identifier** | **str** |  | 
**category** | **str** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.eligibility_criterion import EligibilityCriterion

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityCriterion from a JSON string
eligibility_criterion_instance = EligibilityCriterion.from_json(json)
# print the JSON string representation of the object
print(EligibilityCriterion.to_json())

# convert the object into a dict
eligibility_criterion_dict = eligibility_criterion_instance.to_dict()
# create an instance of EligibilityCriterion from a dict
eligibility_criterion_from_dict = EligibilityCriterion.from_dict(eligibility_criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


