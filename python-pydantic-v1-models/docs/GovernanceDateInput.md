# GovernanceDateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**Code**](Code.md) |  | 
**date_value** | **date** |  | 
**geographic_scopes** | [**List[GeographicScopeInput]**](GeographicScopeInput.md) |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.governance_date_input import GovernanceDateInput

# TODO update the JSON string below
json = "{}"
# create an instance of GovernanceDateInput from a JSON string
governance_date_input_instance = GovernanceDateInput.from_json(json)
# print the JSON string representation of the object
print GovernanceDateInput.to_json()

# convert the object into a dict
governance_date_input_dict = governance_date_input_instance.to_dict()
# create an instance of GovernanceDateInput from a dict
governance_date_input_from_dict = GovernanceDateInput.from_dict(governance_date_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


