# Code

NCI C-Code: C25162 Definition: A symbol or combination of symbols which is assigned to the members of a collection. Preferred Term: Code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** |  | 
**code_system** | **str** |  | 
**code_system_version** | **str** |  | 
**decode** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.code import Code

# TODO update the JSON string below
json = "{}"
# create an instance of Code from a JSON string
code_instance = Code.from_json(json)
# print the JSON string representation of the object
print(Code.to_json())

# convert the object into a dict
code_dict = code_instance.to_dict()
# create an instance of Code from a dict
code_from_dict = Code.from_dict(code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


