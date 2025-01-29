# ProductOrganizationRole

NCI C-Code: CNEW Definition: A designation that identifies the function of an organization within the context of the product. Preferred Term: Product Organization Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**applies_to** | **List[str]** |  | [optional] 
**code** | **str** |  | 
**organization** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.product_organization_role import ProductOrganizationRole

# TODO update the JSON string below
json = "{}"
# create an instance of ProductOrganizationRole from a JSON string
product_organization_role_instance = ProductOrganizationRole.from_json(json)
# print the JSON string representation of the object
print ProductOrganizationRole.to_json()

# convert the object into a dict
product_organization_role_dict = product_organization_role_instance.to_dict()
# create an instance of ProductOrganizationRole from a dict
product_organization_role_from_dict = ProductOrganizationRole.from_dict(product_organization_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


