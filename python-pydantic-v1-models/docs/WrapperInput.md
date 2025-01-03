# WrapperInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study** | [**StudyInput**](StudyInput.md) |  | 
**usdm_version** | **str** |  | 
**system_name** | **str** |  | [optional] 
**system_version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.wrapper_input import WrapperInput

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperInput from a JSON string
wrapper_input_instance = WrapperInput.from_json(json)
# print the JSON string representation of the object
print WrapperInput.to_json()

# convert the object into a dict
wrapper_input_dict = wrapper_input_instance.to_dict()
# create an instance of WrapperInput from a dict
wrapper_input_from_dict = WrapperInput.from_dict(wrapper_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


