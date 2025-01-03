# StudySite


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**country** | [**Code**](Code.md) |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_site import StudySite

# TODO update the JSON string below
json = "{}"
# create an instance of StudySite from a JSON string
study_site_instance = StudySite.from_json(json)
# print the JSON string representation of the object
print StudySite.to_json()

# convert the object into a dict
study_site_dict = study_site_instance.to_dict()
# create an instance of StudySite from a dict
study_site_from_dict = StudySite.from_dict(study_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


