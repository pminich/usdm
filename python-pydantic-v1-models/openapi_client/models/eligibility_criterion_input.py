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
from openapi_client.models.comment_annotation import CommentAnnotation

class EligibilityCriterionInput(BaseModel):
    """
    EligibilityCriterionInput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    text: StrictStr = Field(...)
    dictionary_id: Optional[StrictStr] = Field(default=None, alias="dictionaryId")
    notes: Optional[conlist(CommentAnnotation)] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    category: Code = Field(...)
    identifier: StrictStr = Field(...)
    next_id: Optional[StrictStr] = Field(default=None, alias="nextId")
    previous_id: Optional[StrictStr] = Field(default=None, alias="previousId")
    __properties = ["id", "name", "label", "description", "text", "dictionaryId", "notes", "instanceType", "category", "identifier", "nextId", "previousId"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('EligibilityCriterion',):
            raise ValueError("must be one of enum values ('EligibilityCriterion')")
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
    def from_json(cls, json_str: str) -> EligibilityCriterionInput:
        """Create an instance of EligibilityCriterionInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if dictionary_id (nullable) is None
        # and __fields_set__ contains the field
        if self.dictionary_id is None and "dictionary_id" in self.__fields_set__:
            _dict['dictionaryId'] = None

        # set to None if next_id (nullable) is None
        # and __fields_set__ contains the field
        if self.next_id is None and "next_id" in self.__fields_set__:
            _dict['nextId'] = None

        # set to None if previous_id (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_id is None and "previous_id" in self.__fields_set__:
            _dict['previousId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EligibilityCriterionInput:
        """Create an instance of EligibilityCriterionInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EligibilityCriterionInput.parse_obj(obj)

        _obj = EligibilityCriterionInput.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "text": obj.get("text"),
            "dictionary_id": obj.get("dictionaryId"),
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "instance_type": obj.get("instanceType"),
            "category": Code.from_dict(obj.get("category")) if obj.get("category") is not None else None,
            "identifier": obj.get("identifier"),
            "next_id": obj.get("nextId"),
            "previous_id": obj.get("previousId")
        })
        return _obj


