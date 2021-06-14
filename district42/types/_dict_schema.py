from typing import Any, Dict

from niltype import Nil, Nilable

from .._props import Props
from .._schema_visitor import SchemaVisitor
from .._schema_visitor import SchemaVisitorReturnType as ReturnType
from ..errors import DeclarationError, make_already_declared_error, make_invalid_type_error
from ..utils import is_ellipsis
from ._schema import GenericSchema, Schema

__all__ = ("DictSchema", "DictProps",)


class DictProps(Props):
    @property
    def keys(self) -> Nilable[Dict[Any, GenericSchema]]:
        return self.get("keys")


class DictSchema(Schema[DictProps]):
    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        return visitor.visit_dict(self, **kwargs)

    def __call__(self, /, keys: Dict[Any, GenericSchema]) -> "DictSchema":
        if not isinstance(keys, dict):
            raise make_invalid_type_error(self, keys, (dict,))

        if self.props.keys is not Nil:
            raise make_already_declared_error(self)

        for key, val in keys.items():
            if is_ellipsis(key) or is_ellipsis(val):
                if not is_ellipsis(key):
                    message = f"Inappropriate type of key {key!r} ({type(key)!r})"
                    raise DeclarationError(message)
                if not is_ellipsis(val):
                    message = f"Inappropriate type of value {val!r} ({type(val)!r})"
                    raise DeclarationError(message)
            else:
                if not isinstance(val, Schema):
                    raise make_invalid_type_error(self, val, (Schema,))

        return self.__class__(self.props.update(keys=keys))

    def __getitem__(self, /, key: Any) -> GenericSchema:
        if (self.props.keys is Nil) or (key not in self.props.keys) or (is_ellipsis(key)):
            key_repr = "..." if is_ellipsis(key) else key
            raise KeyError(key_repr)
        return self.props.keys[key]
