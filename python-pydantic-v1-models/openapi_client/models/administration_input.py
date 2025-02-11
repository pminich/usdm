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
from openapi_client.models.administration_duration_input import AdministrationDurationInput
from openapi_client.models.alias_code import AliasCode
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.quantity_input import QuantityInput

class AdministrationInput(BaseModel):
    """
    AdministrationInput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    duration: AdministrationDurationInput = Field(...)
    dose: Optional[QuantityInput] = Field(...)
    route: Optional[AliasCode] = Field(...)
    frequency: Optional[AliasCode] = Field(...)
    administrable_product_id: Optional[StrictStr] = Field(default=None, alias="administrableProductId")
    medical_device_id: Optional[StrictStr] = Field(default=None, alias="medicalDeviceId")
    notes: Optional[conlist(CommentAnnotation)] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "duration", "dose", "route", "frequency", "administrableProductId", "medicalDeviceId", "notes", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Administration',):
            raise ValueError("must be one of enum values ('Administration')")
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
    def from_json(cls, json_str: str) -> AdministrationInput:
        """Create an instance of AdministrationInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dose
        if self.dose:
            _dict['dose'] = self.dose.to_dict()
        # override the default output from pydantic by calling `to_dict()` of route
        if self.route:
            _dict['route'] = self.route.to_dict()
        # override the default output from pydantic by calling `to_dict()` of frequency
        if self.frequency:
            _dict['frequency'] = self.frequency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if dose (nullable) is None
        # and __fields_set__ contains the field
        if self.dose is None and "dose" in self.__fields_set__:
            _dict['dose'] = None

        # set to None if route (nullable) is None
        # and __fields_set__ contains the field
        if self.route is None and "route" in self.__fields_set__:
            _dict['route'] = None

        # set to None if frequency (nullable) is None
        # and __fields_set__ contains the field
        if self.frequency is None and "frequency" in self.__fields_set__:
            _dict['frequency'] = None

        # set to None if administrable_product_id (nullable) is None
        # and __fields_set__ contains the field
        if self.administrable_product_id is None and "administrable_product_id" in self.__fields_set__:
            _dict['administrableProductId'] = None

        # set to None if medical_device_id (nullable) is None
        # and __fields_set__ contains the field
        if self.medical_device_id is None and "medical_device_id" in self.__fields_set__:
            _dict['medicalDeviceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdministrationInput:
        """Create an instance of AdministrationInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdministrationInput.parse_obj(obj)

        _obj = AdministrationInput.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "duration": AdministrationDurationInput.from_dict(obj.get("duration")) if obj.get("duration") is not None else None,
            "dose": QuantityInput.from_dict(obj.get("dose")) if obj.get("dose") is not None else None,
            "route": AliasCode.from_dict(obj.get("route")) if obj.get("route") is not None else None,
            "frequency": AliasCode.from_dict(obj.get("frequency")) if obj.get("frequency") is not None else None,
            "administrable_product_id": obj.get("administrableProductId"),
            "medical_device_id": obj.get("medicalDeviceId"),
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


