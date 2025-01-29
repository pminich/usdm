# AdministrationDuration

NCI C-Code: C69282 Definition: The amount of time elapsed during the administration of an agent. Preferred Term: Administration Duration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | 
**duration_will_vary** | **str** |  | 
**reason_duration_will_vary** | **str** |  | 
**quantity** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.administration_duration import AdministrationDuration

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrationDuration from a JSON string
administration_duration_instance = AdministrationDuration.from_json(json)
# print the JSON string representation of the object
print AdministrationDuration.to_json()

# convert the object into a dict
administration_duration_dict = administration_duration_instance.to_dict()
# create an instance of AdministrationDuration from a dict
administration_duration_from_dict = AdministrationDuration.from_dict(administration_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


