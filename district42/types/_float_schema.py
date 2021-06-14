from typing import Any

from niltype import Nil, Nilable

from .._props import Props
from .._schema_visitor import SchemaVisitor
from .._schema_visitor import SchemaVisitorReturnType as ReturnType
from ..errors import (
    make_already_declared_error,
    make_incorrect_max_error,
    make_incorrect_min_error,
    make_invalid_type_error,
)
from ._schema import Schema

__all__ = ("FloatSchema", "FloatProps",)


class FloatProps(Props):
    @property
    def value(self) -> Nilable[float]:
        return self.get("value")

    @property
    def min(self) -> Nilable[float]:
        return self.get("min")

    @property
    def max(self) -> Nilable[float]:
        return self.get("max")


class FloatSchema(Schema[FloatProps]):
    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        return visitor.visit_float(self, **kwargs)

    def __call__(self, /, value: float) -> "FloatSchema":
        if not isinstance(value, float):
            raise make_invalid_type_error(self, value, (float,))

        if self.props.value is not Nil:
            raise make_already_declared_error(self)

        if (self.props.min is not Nil) or (self.props.max is not Nil):
            raise make_already_declared_error(self)

        return self.__class__(self.props.update(value=value))

    def min(self, /, value: float) -> "FloatSchema":
        if not isinstance(value, float):
            raise make_invalid_type_error(self, value, (float,))

        if self.props.min is not Nil:
            raise make_already_declared_error(self)

        if (self.props.value is not Nil) and (value > self.props.value):
            raise make_incorrect_min_error(self, self.props.value, value)

        return self.__class__(self.props.update(min=value))

    def max(self, /, value: float) -> "FloatSchema":
        if not isinstance(value, float):
            raise make_invalid_type_error(self, value, (float,))

        if self.props.max is not Nil:
            raise make_already_declared_error(self)

        if (self.props.value is not Nil) and (value < self.props.value):
            raise make_incorrect_max_error(self, self.props.value, value)

        return self.__class__(self.props.update(max=value))
