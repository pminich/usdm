# AssignedPerson

NCI C-Code: CNEW Definition: An individual person who is allotted or appointed to a particular role, function, or other entity. Preferred Term: Assigned Person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**job_title** | **str** |  | 
**organization** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.assigned_person import AssignedPerson

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedPerson from a JSON string
assigned_person_instance = AssignedPerson.from_json(json)
# print the JSON string representation of the object
print(AssignedPerson.to_json())

# convert the object into a dict
assigned_person_dict = assigned_person_instance.to_dict()
# create an instance of AssignedPerson from a dict
assigned_person_from_dict = AssignedPerson.from_dict(assigned_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


