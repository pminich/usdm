# CommentAnnotation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**codes** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.comment_annotation import CommentAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of CommentAnnotation from a JSON string
comment_annotation_instance = CommentAnnotation.from_json(json)
# print the JSON string representation of the object
print CommentAnnotation.to_json()

# convert the object into a dict
comment_annotation_dict = comment_annotation_instance.to_dict()
# create an instance of CommentAnnotation from a dict
comment_annotation_from_dict = CommentAnnotation.from_dict(comment_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


