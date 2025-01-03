# GeographicScopeInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | [**Code**](Code.md) |  | 
**code** | [**AliasCode**](AliasCode.md) |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.geographic_scope_input import GeographicScopeInput

# TODO update the JSON string below
json = "{}"
# create an instance of GeographicScopeInput from a JSON string
geographic_scope_input_instance = GeographicScopeInput.from_json(json)
# print the JSON string representation of the object
print GeographicScopeInput.to_json()

# convert the object into a dict
geographic_scope_input_dict = geographic_scope_input_instance.to_dict()
# create an instance of GeographicScopeInput from a dict
geographic_scope_input_from_dict = GeographicScopeInput.from_dict(geographic_scope_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


