# ProductOrganizationRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**code** | [**Code**](Code.md) |  | 
**applies_to_ids** | **List[str]** |  | [optional] [default to []]
**organization_id** | **str** |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.product_organization_role import ProductOrganizationRole

# TODO update the JSON string below
json = "{}"
# create an instance of ProductOrganizationRole from a JSON string
product_organization_role_instance = ProductOrganizationRole.from_json(json)
# print the JSON string representation of the object
print(ProductOrganizationRole.to_json())

# convert the object into a dict
product_organization_role_dict = product_organization_role_instance.to_dict()
# create an instance of ProductOrganizationRole from a dict
product_organization_role_from_dict = ProductOrganizationRole.from_dict(product_organization_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


