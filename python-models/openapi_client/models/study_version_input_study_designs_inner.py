# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from openapi_client.models.interventional_study_design_input import InterventionalStudyDesignInput
from openapi_client.models.observational_study_design_input import ObservationalStudyDesignInput
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

STUDYVERSIONINPUTSTUDYDESIGNSINNER_ANY_OF_SCHEMAS = ["InterventionalStudyDesignInput", "ObservationalStudyDesignInput"]

class StudyVersionInputStudyDesignsInner(BaseModel):
    """
    StudyVersionInputStudyDesignsInner
    """

    # data type: InterventionalStudyDesignInput
    anyof_schema_1_validator: Optional[InterventionalStudyDesignInput] = None
    # data type: ObservationalStudyDesignInput
    anyof_schema_2_validator: Optional[ObservationalStudyDesignInput] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[InterventionalStudyDesignInput, ObservationalStudyDesignInput]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "InterventionalStudyDesignInput", "ObservationalStudyDesignInput" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = StudyVersionInputStudyDesignsInner.model_construct()
        error_messages = []
        # validate data type: InterventionalStudyDesignInput
        if not isinstance(v, InterventionalStudyDesignInput):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InterventionalStudyDesignInput`")
        else:
            return v

        # validate data type: ObservationalStudyDesignInput
        if not isinstance(v, ObservationalStudyDesignInput):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationalStudyDesignInput`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in StudyVersionInputStudyDesignsInner with anyOf schemas: InterventionalStudyDesignInput, ObservationalStudyDesignInput. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[InterventionalStudyDesignInput] = None
        try:
            instance.actual_instance = InterventionalStudyDesignInput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ObservationalStudyDesignInput] = None
        try:
            instance.actual_instance = ObservationalStudyDesignInput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into StudyVersionInputStudyDesignsInner with anyOf schemas: InterventionalStudyDesignInput, ObservationalStudyDesignInput. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], InterventionalStudyDesignInput, ObservationalStudyDesignInput]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


