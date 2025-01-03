# QuantityOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **float** |  | 
**unit** | [**AliasCode**](AliasCode.md) |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.quantity_output import QuantityOutput

# TODO update the JSON string below
json = "{}"
# create an instance of QuantityOutput from a JSON string
quantity_output_instance = QuantityOutput.from_json(json)
# print the JSON string representation of the object
print QuantityOutput.to_json()

# convert the object into a dict
quantity_output_dict = quantity_output_instance.to_dict()
# create an instance of QuantityOutput from a dict
quantity_output_from_dict = QuantityOutput.from_dict(quantity_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


