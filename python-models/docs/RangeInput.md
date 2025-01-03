# RangeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**min_value** | **float** |  | 
**max_value** | **float** |  | 
**unit** | [**AliasCode**](AliasCode.md) |  | [optional] 
**is_approximate** | **bool** |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.range_input import RangeInput

# TODO update the JSON string below
json = "{}"
# create an instance of RangeInput from a JSON string
range_input_instance = RangeInput.from_json(json)
# print the JSON string representation of the object
print(RangeInput.to_json())

# convert the object into a dict
range_input_dict = range_input_instance.to_dict()
# create an instance of RangeInput from a dict
range_input_from_dict = RangeInput.from_dict(range_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


