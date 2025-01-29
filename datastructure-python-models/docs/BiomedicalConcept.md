# BiomedicalConcept

NCI C-Code: C201345 Definition: A unit of biomedical knowledge created from a unique combination of characteristics that include implementation details like variables and terminologies, used as building blocks for standardized, hierarchically structured clinical research information. Preferred Term: Biomedical Concept

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**synonyms** | **str** |  | 
**reference** | **str** |  | 
**code** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**properties** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.biomedical_concept import BiomedicalConcept

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConcept from a JSON string
biomedical_concept_instance = BiomedicalConcept.from_json(json)
# print the JSON string representation of the object
print(BiomedicalConcept.to_json())

# convert the object into a dict
biomedical_concept_dict = biomedical_concept_instance.to_dict()
# create an instance of BiomedicalConcept from a dict
biomedical_concept_from_dict = BiomedicalConcept.from_dict(biomedical_concept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


