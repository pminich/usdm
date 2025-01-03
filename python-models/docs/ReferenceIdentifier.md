# ReferenceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**scope_id** | **str** |  | 
**instance_type** | **str** |  | 
**type** | [**Code**](Code.md) |  | 

## Example

```python
from openapi_client.models.reference_identifier import ReferenceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceIdentifier from a JSON string
reference_identifier_instance = ReferenceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ReferenceIdentifier.to_json())

# convert the object into a dict
reference_identifier_dict = reference_identifier_instance.to_dict()
# create an instance of ReferenceIdentifier from a dict
reference_identifier_from_dict = ReferenceIdentifier.from_dict(reference_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

