# IngredientOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | [**Code**](Code.md) |  | 
**substance** | [**SubstanceOutput**](SubstanceOutput.md) |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.ingredient_output import IngredientOutput

# TODO update the JSON string below
json = "{}"
# create an instance of IngredientOutput from a JSON string
ingredient_output_instance = IngredientOutput.from_json(json)
# print the JSON string representation of the object
print IngredientOutput.to_json()

# convert the object into a dict
ingredient_output_dict = ingredient_output_instance.to_dict()
# create an instance of IngredientOutput from a dict
ingredient_output_from_dict = IngredientOutput.from_dict(ingredient_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


