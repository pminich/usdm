# ProcedureInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**procedure_type** | **str** |  | 
**code** | [**Code**](Code.md) |  | 
**study_intervention_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.procedure_input import ProcedureInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProcedureInput from a JSON string
procedure_input_instance = ProcedureInput.from_json(json)
# print the JSON string representation of the object
print(ProcedureInput.to_json())

# convert the object into a dict
procedure_input_dict = procedure_input_instance.to_dict()
# create an instance of ProcedureInput from a dict
procedure_input_from_dict = ProcedureInput.from_dict(procedure_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


