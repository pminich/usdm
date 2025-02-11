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
from openapi_client.models.administrable_product_identifier import AdministrableProductIdentifier
from openapi_client.models.administrable_product_property_output import AdministrableProductPropertyOutput
from openapi_client.models.alias_code import AliasCode
from openapi_client.models.code import Code
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.ingredient_output import IngredientOutput

class AdministrableProductOutput(BaseModel):
    """
    AdministrableProductOutput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    pharmacologic_class: Optional[Code] = Field(default=None, alias="pharmacologicClass")
    administrable_dose_form: Optional[AliasCode] = Field(default=..., alias="administrableDoseForm")
    product_designation: Code = Field(default=..., alias="productDesignation")
    sourcing: Optional[Code] = None
    properties: Optional[conlist(AdministrableProductPropertyOutput)] = None
    identifiers: Optional[conlist(AdministrableProductIdentifier)] = None
    ingredients: Optional[conlist(IngredientOutput)] = None
    notes: Optional[conlist(CommentAnnotation)] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "pharmacologicClass", "administrableDoseForm", "productDesignation", "sourcing", "properties", "identifiers", "ingredients", "notes", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('AdministrableProduct',):
            raise ValueError("must be one of enum values ('AdministrableProduct')")
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
    def from_json(cls, json_str: str) -> AdministrableProductOutput:
        """Create an instance of AdministrableProductOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pharmacologic_class
        if self.pharmacologic_class:
            _dict['pharmacologicClass'] = self.pharmacologic_class.to_dict()
        # override the default output from pydantic by calling `to_dict()` of administrable_dose_form
        if self.administrable_dose_form:
            _dict['administrableDoseForm'] = self.administrable_dose_form.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_designation
        if self.product_designation:
            _dict['productDesignation'] = self.product_designation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sourcing
        if self.sourcing:
            _dict['sourcing'] = self.sourcing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item in self.properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in identifiers (list)
        _items = []
        if self.identifiers:
            for _item in self.identifiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ingredients (list)
        _items = []
        if self.ingredients:
            for _item in self.ingredients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ingredients'] = _items
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

        # set to None if pharmacologic_class (nullable) is None
        # and __fields_set__ contains the field
        if self.pharmacologic_class is None and "pharmacologic_class" in self.__fields_set__:
            _dict['pharmacologicClass'] = None

        # set to None if administrable_dose_form (nullable) is None
        # and __fields_set__ contains the field
        if self.administrable_dose_form is None and "administrable_dose_form" in self.__fields_set__:
            _dict['administrableDoseForm'] = None

        # set to None if sourcing (nullable) is None
        # and __fields_set__ contains the field
        if self.sourcing is None and "sourcing" in self.__fields_set__:
            _dict['sourcing'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdministrableProductOutput:
        """Create an instance of AdministrableProductOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdministrableProductOutput.parse_obj(obj)

        _obj = AdministrableProductOutput.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "pharmacologic_class": Code.from_dict(obj.get("pharmacologicClass")) if obj.get("pharmacologicClass") is not None else None,
            "administrable_dose_form": AliasCode.from_dict(obj.get("administrableDoseForm")) if obj.get("administrableDoseForm") is not None else None,
            "product_designation": Code.from_dict(obj.get("productDesignation")) if obj.get("productDesignation") is not None else None,
            "sourcing": Code.from_dict(obj.get("sourcing")) if obj.get("sourcing") is not None else None,
            "properties": [AdministrableProductPropertyOutput.from_dict(_item) for _item in obj.get("properties")] if obj.get("properties") is not None else None,
            "identifiers": [AdministrableProductIdentifier.from_dict(_item) for _item in obj.get("identifiers")] if obj.get("identifiers") is not None else None,
            "ingredients": [IngredientOutput.from_dict(_item) for _item in obj.get("ingredients")] if obj.get("ingredients") is not None else None,
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


