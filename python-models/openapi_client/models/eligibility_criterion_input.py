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
from openapi_client.models.comment_annotation import CommentAnnotation
from typing import Optional, Set
from typing_extensions import Self

class EligibilityCriterionInput(BaseModel):
    """
    EligibilityCriterionInput
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True)]
    name: Annotated[str, Field(min_length=1, strict=True)]
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    text: StrictStr
    dictionary_id: Optional[StrictStr] = Field(default=None, alias="dictionaryId")
    notes: Optional[List[CommentAnnotation]] = None
    instance_type: StrictStr = Field(alias="instanceType")
    category: Code
    identifier: StrictStr
    next_id: Optional[StrictStr] = Field(default=None, alias="nextId")
    previous_id: Optional[StrictStr] = Field(default=None, alias="previousId")
    __properties: ClassVar[List[str]] = ["id", "name", "label", "description", "text", "dictionaryId", "notes", "instanceType", "category", "identifier", "nextId", "previousId"]

    @field_validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['EligibilityCriterion']):
            raise ValueError("must be one of enum values ('EligibilityCriterion')")
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
        """Create an instance of EligibilityCriterionInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if dictionary_id (nullable) is None
        # and model_fields_set contains the field
        if self.dictionary_id is None and "dictionary_id" in self.model_fields_set:
            _dict['dictionaryId'] = None

        # set to None if next_id (nullable) is None
        # and model_fields_set contains the field
        if self.next_id is None and "next_id" in self.model_fields_set:
            _dict['nextId'] = None

        # set to None if previous_id (nullable) is None
        # and model_fields_set contains the field
        if self.previous_id is None and "previous_id" in self.model_fields_set:
            _dict['previousId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EligibilityCriterionInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "text": obj.get("text"),
            "dictionaryId": obj.get("dictionaryId"),
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None,
            "instanceType": obj.get("instanceType"),
            "category": Code.from_dict(obj["category"]) if obj.get("category") is not None else None,
            "identifier": obj.get("identifier"),
            "nextId": obj.get("nextId"),
            "previousId": obj.get("previousId")
        })
        return _obj


