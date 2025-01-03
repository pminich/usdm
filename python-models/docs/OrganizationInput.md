# OrganizationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**type** | [**Code**](Code.md) |  | 
**identifier_scheme** | **str** |  | 
**identifier** | **str** |  | 
**legal_address** | [**Address**](Address.md) |  | [optional] 
**managed_sites** | [**List[StudySite]**](StudySite.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.organization_input import OrganizationInput

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInput from a JSON string
organization_input_instance = OrganizationInput.from_json(json)
# print the JSON string representation of the object
print(OrganizationInput.to_json())

# convert the object into a dict
organization_input_dict = organization_input_instance.to_dict()
# create an instance of OrganizationInput from a dict
organization_input_from_dict = OrganizationInput.from_dict(organization_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


