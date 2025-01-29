# BiomedicalConceptCategory

NCI C-Code: C201346 Definition: A grouping of biomedical concepts based on some commonality or by user defined characteristics. Preferred Term: Biomedical Concept Category

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**code** | **str** |  | [optional] 
**members** | **List[str]** |  | [optional] 
**children** | **List[str]** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.biomedical_concept_category import BiomedicalConceptCategory

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptCategory from a JSON string
biomedical_concept_category_instance = BiomedicalConceptCategory.from_json(json)
# print the JSON string representation of the object
print BiomedicalConceptCategory.to_json()

# convert the object into a dict
biomedical_concept_category_dict = biomedical_concept_category_instance.to_dict()
# create an instance of BiomedicalConceptCategory from a dict
biomedical_concept_category_from_dict = BiomedicalConceptCategory.from_dict(biomedical_concept_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


