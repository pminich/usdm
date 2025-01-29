# GeographicScope

NCI C-Code: C207591 Definition: The extent or range related to the physical location of an entity. Preferred Term: Geographic Scope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** |  | [optional] 
**type** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.geographic_scope import GeographicScope

# TODO update the JSON string below
json = "{}"
# create an instance of GeographicScope from a JSON string
geographic_scope_instance = GeographicScope.from_json(json)
# print the JSON string representation of the object
print(GeographicScope.to_json())

# convert the object into a dict
geographic_scope_dict = geographic_scope_instance.to_dict()
# create an instance of GeographicScope from a dict
geographic_scope_from_dict = GeographicScope.from_dict(geographic_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


