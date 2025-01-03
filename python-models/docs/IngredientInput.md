# IngredientInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | [**Code**](Code.md) |  | 
**substance** | [**SubstanceInput**](SubstanceInput.md) |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.ingredient_input import IngredientInput

# TODO update the JSON string below
json = "{}"
# create an instance of IngredientInput from a JSON string
ingredient_input_instance = IngredientInput.from_json(json)
# print the JSON string representation of the object
print(IngredientInput.to_json())

# convert the object into a dict
ingredient_input_dict = ingredient_input_instance.to_dict()
# create an instance of IngredientInput from a dict
ingredient_input_from_dict = IngredientInput.from_dict(ingredient_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


