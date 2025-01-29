# Procedure

NCI C-Code: C98769 Definition: Any activity performed by manual and/or instrumental means for the purpose of diagnosis, assessment, therapy, prevention, or palliative care. Preferred Term: Procedure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**procedure_type** | **str** |  | 
**code** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**study_intervention** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.procedure import Procedure

# TODO update the JSON string below
json = "{}"
# create an instance of Procedure from a JSON string
procedure_instance = Procedure.from_json(json)
# print the JSON string representation of the object
print(Procedure.to_json())

# convert the object into a dict
procedure_dict = procedure_instance.to_dict()
# create an instance of Procedure from a dict
procedure_from_dict = Procedure.from_dict(procedure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


