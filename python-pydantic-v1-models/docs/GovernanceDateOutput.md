# GovernanceDateOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**Code**](Code.md) |  | 
**date_value** | **date** |  | 
**geographic_scopes** | [**List[GeographicScopeOutput]**](GeographicScopeOutput.md) |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.governance_date_output import GovernanceDateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GovernanceDateOutput from a JSON string
governance_date_output_instance = GovernanceDateOutput.from_json(json)
# print the JSON string representation of the object
print GovernanceDateOutput.to_json()

# convert the object into a dict
governance_date_output_dict = governance_date_output_instance.to_dict()
# create an instance of GovernanceDateOutput from a dict
governance_date_output_from_dict = GovernanceDateOutput.from_dict(governance_date_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


