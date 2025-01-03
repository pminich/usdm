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
from openapi_client.models.quantity_output import QuantityOutput
from openapi_client.models.range_output import RangeOutput
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

NUMERATOR1_ANY_OF_SCHEMAS = ["QuantityOutput", "RangeOutput"]

class Numerator1(BaseModel):
    """
    Numerator1
    """

    # data type: QuantityOutput
    anyof_schema_1_validator: Optional[QuantityOutput] = None
    # data type: RangeOutput
    anyof_schema_2_validator: Optional[RangeOutput] = None
    if TYPE_CHECKING:
        actual_instance: Union[QuantityOutput, RangeOutput]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(NUMERATOR1_ANY_OF_SCHEMAS, const=True)

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

        instance = Numerator1.construct()
        error_messages = []
        # validate data type: QuantityOutput
        if not isinstance(v, QuantityOutput):
            error_messages.append(f"Error! Input type `{type(v)}` is not `QuantityOutput`")
        else:
            return v

        # validate data type: RangeOutput
        if not isinstance(v, RangeOutput):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RangeOutput`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Numerator1 with anyOf schemas: QuantityOutput, RangeOutput. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Numerator1:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Numerator1:
        """Returns the object represented by the json string"""
        instance = Numerator1.construct()
        if json_str is None:
            return instance

        error_messages = []
        # anyof_schema_1_validator: Optional[QuantityOutput] = None
        try:
            instance.actual_instance = QuantityOutput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[RangeOutput] = None
        try:
            instance.actual_instance = RangeOutput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Numerator1 with anyOf schemas: QuantityOutput, RangeOutput. Details: " + ", ".join(error_messages))
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

