# Quantity

NCI C-Code: C25256 Definition: How much there is of something that can be measured; the total amount or number. Preferred Term: Quantity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **str** |  | 
**unit** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.quantity import Quantity

# TODO update the JSON string below
json = "{}"
# create an instance of Quantity from a JSON string
quantity_instance = Quantity.from_json(json)
# print the JSON string representation of the object
print Quantity.to_json()

# convert the object into a dict
quantity_dict = quantity_instance.to_dict()
# create an instance of Quantity from a dict
quantity_from_dict = Quantity.from_dict(quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


