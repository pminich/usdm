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
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator

class BiospecimenRetention(BaseModel):
    """
    BiospecimenRetention
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    is_retained: StrictBool = Field(default=..., alias="isRetained")
    includes_dna: Optional[StrictBool] = Field(default=None, alias="includesDNA")
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "isRetained", "includesDNA", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('BiospecimenRetention',):
            raise ValueError("must be one of enum values ('BiospecimenRetention')")
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
    def from_json(cls, json_str: str) -> BiospecimenRetention:
        """Create an instance of BiospecimenRetention from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if includes_dna (nullable) is None
        # and __fields_set__ contains the field
        if self.includes_dna is None and "includes_dna" in self.__fields_set__:
            _dict['includesDNA'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BiospecimenRetention:
        """Create an instance of BiospecimenRetention from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BiospecimenRetention.parse_obj(obj)

        _obj = BiospecimenRetention.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "is_retained": obj.get("isRetained"),
            "includes_dna": obj.get("includesDNA"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


