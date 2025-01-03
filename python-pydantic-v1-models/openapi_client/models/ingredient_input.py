# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.code import Code
from openapi_client.models.substance_input import SubstanceInput

class IngredientInput(BaseModel):
    """
    IngredientInput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    role: Code = Field(...)
    substance: SubstanceInput = Field(...)
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "role", "substance", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Ingredient',):
            raise ValueError("must be one of enum values ('Ingredient')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IngredientInput:
        """Create an instance of IngredientInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of substance
        if self.substance:
            _dict['substance'] = self.substance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IngredientInput:
        """Create an instance of IngredientInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IngredientInput.parse_obj(obj)

        _obj = IngredientInput.parse_obj({
            "id": obj.get("id"),
            "role": Code.from_dict(obj.get("role")) if obj.get("role") is not None else None,
            "substance": SubstanceInput.from_dict(obj.get("substance")) if obj.get("substance") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


