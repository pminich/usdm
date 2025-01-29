# Activity

NCI C-Code: C71473 Definition: An action, undertaking, or event, which is anticipated to be performed or observed, or was performed or observed, according to the study protocol during the execution of the study. Preferred Term: Study Activity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**defined_procedures** | **List[str]** |  | [optional] 
**biomedical_concepts** | **List[str]** |  | [optional] 
**next** | **str** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**timeline** | **str** |  | [optional] 
**children** | **List[str]** |  | [optional] 
**previous** | **str** |  | [optional] 
**bc_surrogates** | **List[str]** |  | [optional] 
**bc_categories** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print Activity.to_json()

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_from_dict = Activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


