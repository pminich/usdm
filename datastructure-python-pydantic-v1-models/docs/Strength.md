# Strength

NCI C-Code: CNEW Definition: The content of an substance expressed quantitatively per dosage unit, per unit of volume, or per unit of weight, according to the pharmaceutical dose form of the product. Preferred Term: Substance Strength

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**numerator** | **str** |  | [optional] 
**denominator** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.strength import Strength

# TODO update the JSON string below
json = "{}"
# create an instance of Strength from a JSON string
strength_instance = Strength.from_json(json)
# print the JSON string representation of the object
print Strength.to_json()

# convert the object into a dict
strength_dict = strength_instance.to_dict()
# create an instance of Strength from a dict
strength_from_dict = Strength.from_dict(strength_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


