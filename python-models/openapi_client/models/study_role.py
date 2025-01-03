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
from openapi_client.models.assigned_person import AssignedPerson
from openapi_client.models.code import Code
from openapi_client.models.masking import Masking
from typing import Optional, Set
from typing_extensions import Self

class StudyRole(BaseModel):
    """
    StudyRole
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True)]
    name: Annotated[str, Field(min_length=1, strict=True)]
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    code: Code
    applies_to_ids: Optional[List[StrictStr]] = Field(default=None, alias="appliesToIds")
    assigned_persons: Optional[List[AssignedPerson]] = Field(default=None, alias="assignedPersons")
    organization_ids: Optional[List[Optional[StrictStr]]] = Field(default=None, alias="organizationIds")
    masking: Optional[Masking] = None
    instance_type: StrictStr = Field(alias="instanceType")
    __properties: ClassVar[List[str]] = ["id", "name", "label", "description", "code", "appliesToIds", "assignedPersons", "organizationIds", "masking", "instanceType"]

    @field_validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['StudyRole']):
            raise ValueError("must be one of enum values ('StudyRole')")
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
        """Create an instance of StudyRole from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of code
        if self.code:
            _dict['code'] = self.code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assigned_persons (list)
        _items = []
        if self.assigned_persons:
            for _item_assigned_persons in self.assigned_persons:
                if _item_assigned_persons:
                    _items.append(_item_assigned_persons.to_dict())
            _dict['assignedPersons'] = _items
        # override the default output from pydantic by calling `to_dict()` of masking
        if self.masking:
            _dict['masking'] = self.masking.to_dict()
        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if masking (nullable) is None
        # and model_fields_set contains the field
        if self.masking is None and "masking" in self.model_fields_set:
            _dict['masking'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StudyRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "code": Code.from_dict(obj["code"]) if obj.get("code") is not None else None,
            "appliesToIds": obj.get("appliesToIds"),
            "assignedPersons": [AssignedPerson.from_dict(_item) for _item in obj["assignedPersons"]] if obj.get("assignedPersons") is not None else None,
            "organizationIds": obj.get("organizationIds"),
            "masking": Masking.from_dict(obj["masking"]) if obj.get("masking") is not None else None,
            "instanceType": obj.get("instanceType")
        })
        return _obj

