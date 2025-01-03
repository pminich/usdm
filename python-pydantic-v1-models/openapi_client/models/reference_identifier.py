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

class ReferenceIdentifier(BaseModel):
    """
    ReferenceIdentifier
    """
    id: constr(strict=True, min_length=1) = Field(...)
    text: StrictStr = Field(...)
    scope_id: StrictStr = Field(default=..., alias="scopeId")
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    type: Code = Field(...)
    __properties = ["id", "text", "scopeId", "instanceType", "type"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ReferenceIdentifier',):
            raise ValueError("must be one of enum values ('ReferenceIdentifier')")
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
    def from_json(cls, json_str: str) -> ReferenceIdentifier:
        """Create an instance of ReferenceIdentifier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferenceIdentifier:
        """Create an instance of ReferenceIdentifier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferenceIdentifier.parse_obj(obj)

        _obj = ReferenceIdentifier.parse_obj({
            "id": obj.get("id"),
            "text": obj.get("text"),
            "scope_id": obj.get("scopeId"),
            "instance_type": obj.get("instanceType"),
            "type": Code.from_dict(obj.get("type")) if obj.get("type") is not None else None
        })
        return _obj

