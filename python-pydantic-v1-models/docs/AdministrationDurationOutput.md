# AdministrationDurationOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**quantity** | [**QuantityOutput**](QuantityOutput.md) |  | [optional] 
**description** | **str** |  | 
**duration_will_vary** | **bool** |  | 
**reason_duration_will_vary** | **str** |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.administration_duration_output import AdministrationDurationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrationDurationOutput from a JSON string
administration_duration_output_instance = AdministrationDurationOutput.from_json(json)
# print the JSON string representation of the object
print AdministrationDurationOutput.to_json()

# convert the object into a dict
administration_duration_output_dict = administration_duration_output_instance.to_dict()
# create an instance of AdministrationDurationOutput from a dict
administration_duration_output_from_dict = AdministrationDurationOutput.from_dict(administration_duration_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


