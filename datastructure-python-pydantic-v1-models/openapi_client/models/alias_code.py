# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class AliasCode(BaseModel):
    """
    NCI C-Code: C201344 Definition: An alternative symbol or combination of symbols which is assigned to the members of a collection. Preferred Term: Alias Code  # noqa: E501
    """
    id: StrictStr = Field(...)
    standard_code: StrictStr = Field(default=..., alias="standardCode")
    standard_code_aliases: Optional[conlist(StrictStr)] = Field(default=None, alias="standardCodeAliases")
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties = ["id", "standardCode", "standardCodeAliases", "instanceType"]

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
    def from_json(cls, json_str: str) -> AliasCode:
        """Create an instance of AliasCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AliasCode:
        """Create an instance of AliasCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AliasCode.parse_obj(obj)

        _obj = AliasCode.parse_obj({
            "id": obj.get("id"),
            "standard_code": obj.get("standardCode"),
            "standard_code_aliases": obj.get("standardCodeAliases"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


