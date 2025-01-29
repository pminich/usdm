# BiomedicalConceptProperty

NCI C-Code: C202493 Definition: A characteristic from a set of characteristics used to define a biomedical concept. Preferred Term: Biomedical Concept Property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**is_required** | **str** |  | 
**is_enabled** | **str** |  | 
**datatype** | **str** |  | 
**code** | **str** |  | 
**response_codes** | **List[str]** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.biomedical_concept_property import BiomedicalConceptProperty

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptProperty from a JSON string
biomedical_concept_property_instance = BiomedicalConceptProperty.from_json(json)
# print the JSON string representation of the object
print(BiomedicalConceptProperty.to_json())

# convert the object into a dict
biomedical_concept_property_dict = biomedical_concept_property_instance.to_dict()
# create an instance of BiomedicalConceptProperty from a dict
biomedical_concept_property_from_dict = BiomedicalConceptProperty.from_dict(biomedical_concept_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


