# MedicalDeviceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**scope_id** | **str** |  | 
**instance_type** | **str** |  | 
**type** | [**Code**](Code.md) |  | 

## Example

```python
from openapi_client.models.medical_device_identifier import MedicalDeviceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalDeviceIdentifier from a JSON string
medical_device_identifier_instance = MedicalDeviceIdentifier.from_json(json)
# print the JSON string representation of the object
print(MedicalDeviceIdentifier.to_json())

# convert the object into a dict
medical_device_identifier_dict = medical_device_identifier_instance.to_dict()
# create an instance of MedicalDeviceIdentifier from a dict
medical_device_identifier_from_dict = MedicalDeviceIdentifier.from_dict(medical_device_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


