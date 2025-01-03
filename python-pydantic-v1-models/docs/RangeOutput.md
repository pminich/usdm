# RangeOutput


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
from openapi_client.models.range_output import RangeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RangeOutput from a JSON string
range_output_instance = RangeOutput.from_json(json)
# print the JSON string representation of the object
print RangeOutput.to_json()

# convert the object into a dict
range_output_dict = range_output_instance.to_dict()
# create an instance of RangeOutput from a dict
range_output_from_dict = RangeOutput.from_dict(range_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


