# AliasCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**standard_code** | [**Code**](Code.md) |  | 
**standard_code_aliases** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.alias_code import AliasCode

# TODO update the JSON string below
json = "{}"
# create an instance of AliasCode from a JSON string
alias_code_instance = AliasCode.from_json(json)
# print the JSON string representation of the object
print AliasCode.to_json()

# convert the object into a dict
alias_code_dict = alias_code_instance.to_dict()
# create an instance of AliasCode from a dict
alias_code_from_dict = AliasCode.from_dict(alias_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


