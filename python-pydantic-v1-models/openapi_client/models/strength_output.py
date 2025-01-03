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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.numerator1 import Numerator1
from openapi_client.models.quantity_output import QuantityOutput

class StrengthOutput(BaseModel):
    """
    StrengthOutput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    denominator: Optional[QuantityOutput] = None
    numerator: Optional[Numerator1] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "denominator", "numerator", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Strength',):
            raise ValueError("must be one of enum values ('Strength')")
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
    def from_json(cls, json_str: str) -> StrengthOutput:
        """Create an instance of StrengthOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of denominator
        if self.denominator:
            _dict['denominator'] = self.denominator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of numerator
        if self.numerator:
            _dict['numerator'] = self.numerator.to_dict()
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if denominator (nullable) is None
        # and __fields_set__ contains the field
        if self.denominator is None and "denominator" in self.__fields_set__:
            _dict['denominator'] = None

        # set to None if numerator (nullable) is None
        # and __fields_set__ contains the field
        if self.numerator is None and "numerator" in self.__fields_set__:
            _dict['numerator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StrengthOutput:
        """Create an instance of StrengthOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StrengthOutput.parse_obj(obj)

        _obj = StrengthOutput.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "denominator": QuantityOutput.from_dict(obj.get("denominator")) if obj.get("denominator") is not None else None,
            "numerator": Numerator1.from_dict(obj.get("numerator")) if obj.get("numerator") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


