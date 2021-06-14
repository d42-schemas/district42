from typing import Any

from .._props import Props
from .._schema_visitor import SchemaVisitor
from .._schema_visitor import SchemaVisitorReturnType as ReturnType
from ._schema import Schema

__all__ = ("NoneSchema", "NoneProps",)


class NoneProps(Props):
    pass


class NoneSchema(Schema[NoneProps]):
    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        return visitor.visit_none(self, **kwargs)
