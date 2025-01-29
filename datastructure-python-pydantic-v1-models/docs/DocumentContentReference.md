# DocumentContentReference

NCI C-Code: CNEW Definition: A citation pointing to the location of specific content within a document. Preferred Term: Document Content Reference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**section_number** | **str** |  | 
**section_title** | **str** |  | 
**applies_to** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.document_content_reference import DocumentContentReference

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentContentReference from a JSON string
document_content_reference_instance = DocumentContentReference.from_json(json)
# print the JSON string representation of the object
print DocumentContentReference.to_json()

# convert the object into a dict
document_content_reference_dict = document_content_reference_instance.to_dict()
# create an instance of DocumentContentReference from a dict
document_content_reference_from_dict = DocumentContentReference.from_dict(document_content_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


