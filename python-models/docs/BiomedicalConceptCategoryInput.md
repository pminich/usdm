# BiomedicalConceptCategoryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**child_ids** | **List[str]** |  | [optional] [default to []]
**member_ids** | **List[Optional[str]]** |  | [optional] [default to []]
**code** | [**AliasCode**](AliasCode.md) |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.biomedical_concept_category_input import BiomedicalConceptCategoryInput

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptCategoryInput from a JSON string
biomedical_concept_category_input_instance = BiomedicalConceptCategoryInput.from_json(json)
# print the JSON string representation of the object
print(BiomedicalConceptCategoryInput.to_json())

# convert the object into a dict
biomedical_concept_category_input_dict = biomedical_concept_category_input_instance.to_dict()
# create an instance of BiomedicalConceptCategoryInput from a dict
biomedical_concept_category_input_from_dict = BiomedicalConceptCategoryInput.from_dict(biomedical_concept_category_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


