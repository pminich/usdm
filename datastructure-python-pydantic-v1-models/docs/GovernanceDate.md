# GovernanceDate

NCI C-Code: C207595 Definition: Any of the dates associated with event milestones within a clinical study's oversight and management framework. Preferred Term: Study Governance Date

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**date_value** | **str** |  | 
**type** | **str** |  | 
**geographic_scopes** | **List[str]** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.governance_date import GovernanceDate

# TODO update the JSON string below
json = "{}"
# create an instance of GovernanceDate from a JSON string
governance_date_instance = GovernanceDate.from_json(json)
# print the JSON string representation of the object
print GovernanceDate.to_json()

# convert the object into a dict
governance_date_dict = governance_date_instance.to_dict()
# create an instance of GovernanceDate from a dict
governance_date_from_dict = GovernanceDate.from_dict(governance_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


