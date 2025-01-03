# WrapperOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study** | [**StudyOutput**](StudyOutput.md) |  | 
**usdm_version** | **str** |  | 
**system_name** | **str** |  | [optional] 
**system_version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.wrapper_output import WrapperOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperOutput from a JSON string
wrapper_output_instance = WrapperOutput.from_json(json)
# print the JSON string representation of the object
print WrapperOutput.to_json()

# convert the object into a dict
wrapper_output_dict = wrapper_output_instance.to_dict()
# create an instance of WrapperOutput from a dict
wrapper_output_from_dict = WrapperOutput.from_dict(wrapper_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


