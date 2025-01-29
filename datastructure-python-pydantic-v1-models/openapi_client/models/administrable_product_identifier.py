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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class AdministrableProductIdentifier(BaseModel):
    """
    NCI C-Code: CNEW Definition: A sequence of characters used to identify, name, or characterize the administrable product. Preferred Term: Administrable Product Identifier  # noqa: E501
    """
    id: StrictStr = Field(...)
    text: StrictStr = Field(...)
    scope: StrictStr = Field(...)
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties = ["id", "text", "scope", "instanceType"]

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
    def from_json(cls, json_str: str) -> AdministrableProductIdentifier:
        """Create an instance of AdministrableProductIdentifier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdministrableProductIdentifier:
        """Create an instance of AdministrableProductIdentifier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdministrableProductIdentifier.parse_obj(obj)

        _obj = AdministrableProductIdentifier.parse_obj({
            "id": obj.get("id"),
            "text": obj.get("text"),
            "scope": obj.get("scope"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


