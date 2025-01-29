# BiomedicalConceptSurrogate

NCI C-Code: C207590 Definition: A concept that substitutes for a standard biomedical concept from the designated source. Preferred Term: Biomedical Concept Surrogate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**reference** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.biomedical_concept_surrogate import BiomedicalConceptSurrogate

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptSurrogate from a JSON string
biomedical_concept_surrogate_instance = BiomedicalConceptSurrogate.from_json(json)
# print the JSON string representation of the object
print BiomedicalConceptSurrogate.to_json()

# convert the object into a dict
biomedical_concept_surrogate_dict = biomedical_concept_surrogate_instance.to_dict()
# create an instance of BiomedicalConceptSurrogate from a dict
biomedical_concept_surrogate_from_dict = BiomedicalConceptSurrogate.from_dict(biomedical_concept_surrogate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


