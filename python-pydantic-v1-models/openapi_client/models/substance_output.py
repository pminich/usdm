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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from openapi_client.models.code import Code
from openapi_client.models.strength_output import StrengthOutput

class SubstanceOutput(BaseModel):
    """
    SubstanceOutput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    codes: Optional[conlist(Code)] = None
    strengths: conlist(StrengthOutput) = Field(...)
    reference_substance: Optional[SubstanceOutput] = Field(default=None, alias="referenceSubstance")
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "codes", "strengths", "referenceSubstance", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Substance',):
            raise ValueError("must be one of enum values ('Substance')")
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
    def from_json(cls, json_str: str) -> SubstanceOutput:
        """Create an instance of SubstanceOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in codes (list)
        _items = []
        if self.codes:
            for _item in self.codes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['codes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in strengths (list)
        _items = []
        if self.strengths:
            for _item in self.strengths:
                if _item:
                    _items.append(_item.to_dict())
            _dict['strengths'] = _items
        # override the default output from pydantic by calling `to_dict()` of reference_substance
        if self.reference_substance:
            _dict['referenceSubstance'] = self.reference_substance.to_dict()
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if reference_substance (nullable) is None
        # and __fields_set__ contains the field
        if self.reference_substance is None and "reference_substance" in self.__fields_set__:
            _dict['referenceSubstance'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubstanceOutput:
        """Create an instance of SubstanceOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubstanceOutput.parse_obj(obj)

        _obj = SubstanceOutput.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "codes": [Code.from_dict(_item) for _item in obj.get("codes")] if obj.get("codes") is not None else None,
            "strengths": [StrengthOutput.from_dict(_item) for _item in obj.get("strengths")] if obj.get("strengths") is not None else None,
            "reference_substance": SubstanceOutput.from_dict(obj.get("referenceSubstance")) if obj.get("referenceSubstance") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj

SubstanceOutput.update_forward_refs()
