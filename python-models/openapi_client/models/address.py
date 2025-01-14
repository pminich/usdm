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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.code import Code
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True)]
    text: Optional[StrictStr] = None
    lines: Optional[List[Optional[StrictStr]]] = None
    city: Optional[StrictStr] = None
    district: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    country: Optional[Code] = None
    instance_type: StrictStr = Field(alias="instanceType")
    __properties: ClassVar[List[str]] = ["id", "text", "lines", "city", "district", "state", "postalCode", "country", "instanceType"]

    @field_validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Address']):
            raise ValueError("must be one of enum values ('Address')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Address from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if district (nullable) is None
        # and model_fields_set contains the field
        if self.district is None and "district" in self.model_fields_set:
            _dict['district'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.postal_code is None and "postal_code" in self.model_fields_set:
            _dict['postalCode'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "text": obj.get("text"),
            "lines": obj.get("lines"),
            "city": obj.get("city"),
            "district": obj.get("district"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "country": Code.from_dict(obj["country"]) if obj.get("country") is not None else None,
            "instanceType": obj.get("instanceType")
        })
        return _obj


