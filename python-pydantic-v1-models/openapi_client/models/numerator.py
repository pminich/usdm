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

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from openapi_client.models.quantity_input import QuantityInput
from openapi_client.models.range_input import RangeInput
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

NUMERATOR_ANY_OF_SCHEMAS = ["QuantityInput", "RangeInput"]

class Numerator(BaseModel):
    """
    Numerator
    """

    # data type: QuantityInput
    anyof_schema_1_validator: Optional[QuantityInput] = None
    # data type: RangeInput
    anyof_schema_2_validator: Optional[RangeInput] = None
    if TYPE_CHECKING:
        actual_instance: Union[QuantityInput, RangeInput]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(NUMERATOR_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        if v is None:
            return v

        instance = Numerator.construct()
        error_messages = []
        # validate data type: QuantityInput
        if not isinstance(v, QuantityInput):
            error_messages.append(f"Error! Input type `{type(v)}` is not `QuantityInput`")
        else:
            return v

        # validate data type: RangeInput
        if not isinstance(v, RangeInput):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RangeInput`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Numerator with anyOf schemas: QuantityInput, RangeInput. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Numerator:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Numerator:
        """Returns the object represented by the json string"""
        instance = Numerator.construct()
        if json_str is None:
            return instance

        error_messages = []
        # anyof_schema_1_validator: Optional[QuantityInput] = None
        try:
            instance.actual_instance = QuantityInput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[RangeInput] = None
        try:
            instance.actual_instance = RangeInput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Numerator with anyOf schemas: QuantityInput, RangeInput. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

