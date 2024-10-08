import sys
from typing import Any

from niltype import Nil, Nilable

from .._props import Props
from .._schema_visitor import SchemaVisitor
from .._schema_visitor import SchemaVisitorReturnType as ReturnType
from ..errors import make_already_declared_error
from ._schema import Schema

__all__ = ("ConstSchema", "ConstProps",)

if sys.version_info >= (3, 10):
    from typing import TypeAlias


class ConstProps(Props):
    @property
    def value(self) -> Nilable[Any]:
        return self.get("value")


class ConstSchema(Schema[ConstProps]):
    if sys.version_info >= (3, 10):
        type: TypeAlias = Any
    else:
        type: Any = Any

    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        return visitor.visit_const(self, **kwargs)

    def __call__(self, /, value: Any) -> "ConstSchema":
        if self.props.value is not Nil:
            raise make_already_declared_error(self)
        return self.__class__(self.props.update(value=value))
