# ParameterMap

NCI C-Code: C207456 Definition: The paired name and value for a given parameter. Preferred Term: Parameter Map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tag** | **str** |  | 
**reference** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.parameter_map import ParameterMap

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterMap from a JSON string
parameter_map_instance = ParameterMap.from_json(json)
# print the JSON string representation of the object
print(ParameterMap.to_json())

# convert the object into a dict
parameter_map_dict = parameter_map_instance.to_dict()
# create an instance of ParameterMap from a dict
parameter_map_from_dict = ParameterMap.from_dict(parameter_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


