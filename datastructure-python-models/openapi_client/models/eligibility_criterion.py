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

class EligibilityCriterion(BaseModel):
    """
    NCI C-Code: C16112 Definition: Characteristics which are necessary to allow a subject to participate in a clinical study, as outlined in the study protocol. The concept covers inclusion and exclusion criteria. Preferred Term: Study Eligibility Criterion
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    description: StrictStr
    label: StrictStr
    text: StrictStr
    notes: Optional[List[StrictStr]] = None
    dictionary: Optional[StrictStr] = None
    identifier: StrictStr
    category: StrictStr
    next: Optional[StrictStr] = None
    previous: Optional[StrictStr] = None
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "label", "text", "notes", "dictionary", "identifier", "category", "next", "previous", "instanceType"]

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
        """Create an instance of EligibilityCriterion from a JSON string"""
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
        """Create an instance of EligibilityCriterion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "label": obj.get("label"),
            "text": obj.get("text"),
            "notes": obj.get("notes"),
            "dictionary": obj.get("dictionary"),
            "identifier": obj.get("identifier"),
            "category": obj.get("category"),
            "next": obj.get("next"),
            "previous": obj.get("previous"),
            "instanceType": obj.get("instanceType")
        })
        return _obj


