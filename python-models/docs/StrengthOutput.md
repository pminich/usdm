# StrengthOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**denominator** | [**QuantityOutput**](QuantityOutput.md) |  | [optional] 
**numerator** | [**Numerator1**](Numerator1.md) |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.strength_output import StrengthOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StrengthOutput from a JSON string
strength_output_instance = StrengthOutput.from_json(json)
# print the JSON string representation of the object
print(StrengthOutput.to_json())

# convert the object into a dict
strength_output_dict = strength_output_instance.to_dict()
# create an instance of StrengthOutput from a dict
strength_output_from_dict = StrengthOutput.from_dict(strength_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


