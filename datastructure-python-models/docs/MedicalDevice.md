# MedicalDevice

NCI C-Code: C16830 Definition: Any instrument, apparatus, implement, machine, appliance, implant, reagent for in vitro use, software, material or other similar or related article, intended by the manufacturer to be used, alone or in combination for, one or more specific medical purpose(s). [After REGULATION (EU) 2017/745 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 5 April 2017 on medical devices] Preferred Term: Medical Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**hardware_version** | **str** |  | 
**software_version** | **str** |  | 
**embedded_product** | **str** |  | [optional] 
**sourcing** | **str** |  | [optional] 
**notes** | **str** |  | 
**identifiers** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.medical_device import MedicalDevice

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalDevice from a JSON string
medical_device_instance = MedicalDevice.from_json(json)
# print the JSON string representation of the object
print(MedicalDevice.to_json())

# convert the object into a dict
medical_device_dict = medical_device_instance.to_dict()
# create an instance of MedicalDevice from a dict
medical_device_from_dict = MedicalDevice.from_dict(medical_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


