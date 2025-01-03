# BiospecimenRetention


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_retained** | **bool** |  | 
**includes_dna** | **bool** |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.biospecimen_retention import BiospecimenRetention

# TODO update the JSON string below
json = "{}"
# create an instance of BiospecimenRetention from a JSON string
biospecimen_retention_instance = BiospecimenRetention.from_json(json)
# print the JSON string representation of the object
print BiospecimenRetention.to_json()

# convert the object into a dict
biospecimen_retention_dict = biospecimen_retention_instance.to_dict()
# create an instance of BiospecimenRetention from a dict
biospecimen_retention_from_dict = BiospecimenRetention.from_dict(biospecimen_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


