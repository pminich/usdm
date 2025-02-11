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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class StudyDefinitionDocumentVersion(BaseModel):
    """
    NCI C-Code: CNEW Definition: A representation of a particular edition or snapshot of the study definition document as it exists at a particular point in time. Preferred Term: Study Definition Document Version
    """ # noqa: E501
    id: StrictStr
    version: StrictStr
    status: StrictStr
    notes: Optional[List[StrictStr]] = None
    date_values: Optional[List[StrictStr]] = Field(default=None, alias="dateValues")
    contents: Optional[List[StrictStr]] = None
    children: Optional[List[StrictStr]] = None
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties: ClassVar[List[str]] = ["id", "version", "status", "notes", "dateValues", "contents", "children", "instanceType"]

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
        """Create an instance of StudyDefinitionDocumentVersion from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StudyDefinitionDocumentVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "version": obj.get("version"),
            "status": obj.get("status"),
            "notes": obj.get("notes"),
            "dateValues": obj.get("dateValues"),
            "contents": obj.get("contents"),
            "children": obj.get("children"),
            "instanceType": obj.get("instanceType")
        })
        return _obj


