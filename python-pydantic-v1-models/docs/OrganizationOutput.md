# OrganizationOutput


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
from openapi_client.models.organization_output import OrganizationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationOutput from a JSON string
organization_output_instance = OrganizationOutput.from_json(json)
# print the JSON string representation of the object
print OrganizationOutput.to_json()

# convert the object into a dict
organization_output_dict = organization_output_instance.to_dict()
# create an instance of OrganizationOutput from a dict
organization_output_from_dict = OrganizationOutput.from_dict(organization_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


