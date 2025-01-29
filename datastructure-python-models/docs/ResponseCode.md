# ResponseCode

NCI C-Code: C201347 Definition: A symbol or combination of symbols representing the response to the question. Preferred Term: Response Code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_enabled** | **str** |  | 
**code** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.response_code import ResponseCode

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCode from a JSON string
response_code_instance = ResponseCode.from_json(json)
# print the JSON string representation of the object
print(ResponseCode.to_json())

# convert the object into a dict
response_code_dict = response_code_instance.to_dict()
# create an instance of ResponseCode from a dict
response_code_from_dict = ResponseCode.from_dict(response_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


