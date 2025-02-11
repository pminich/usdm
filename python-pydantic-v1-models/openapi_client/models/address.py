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

class Address(BaseModel):
    """
    Address
    """
    id: constr(strict=True, min_length=1) = Field(...)
    text: Optional[StrictStr] = None
    lines: Optional[conlist(StrictStr)] = None
    city: Optional[StrictStr] = None
    district: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    country: Optional[Code] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "text", "lines", "city", "district", "state", "postalCode", "country", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Address',):
            raise ValueError("must be one of enum values ('Address')")
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
    def from_json(cls, json_str: str) -> Address:
        """Create an instance of Address from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # set to None if text (nullable) is None
        # and __fields_set__ contains the field
        if self.text is None and "text" in self.__fields_set__:
            _dict['text'] = None

        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        # set to None if district (nullable) is None
        # and __fields_set__ contains the field
        if self.district is None and "district" in self.__fields_set__:
            _dict['district'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        # set to None if postal_code (nullable) is None
        # and __fields_set__ contains the field
        if self.postal_code is None and "postal_code" in self.__fields_set__:
            _dict['postalCode'] = None

        # set to None if country (nullable) is None
        # and __fields_set__ contains the field
        if self.country is None and "country" in self.__fields_set__:
            _dict['country'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Address:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Address.parse_obj(obj)

        _obj = Address.parse_obj({
            "id": obj.get("id"),
            "text": obj.get("text"),
            "lines": obj.get("lines"),
            "city": obj.get("city"),
            "district": obj.get("district"),
            "state": obj.get("state"),
            "postal_code": obj.get("postalCode"),
            "country": Code.from_dict(obj.get("country")) if obj.get("country") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


