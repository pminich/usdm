# StrengthInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**denominator** | [**QuantityInput**](QuantityInput.md) |  | [optional] 
**numerator** | [**Numerator**](Numerator.md) |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.strength_input import StrengthInput

# TODO update the JSON string below
json = "{}"
# create an instance of StrengthInput from a JSON string
strength_input_instance = StrengthInput.from_json(json)
# print the JSON string representation of the object
print StrengthInput.to_json()

# convert the object into a dict
strength_input_dict = strength_input_instance.to_dict()
# create an instance of StrengthInput from a dict
strength_input_from_dict = StrengthInput.from_dict(strength_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


