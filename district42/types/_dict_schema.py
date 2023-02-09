from typing import Any, Dict, KeysView, List, Set, Tuple, Union

from niltype import Nil, Nilable

from .._props import Props
from .._schema_visitor import SchemaVisitor
from .._schema_visitor import SchemaVisitorReturnType as ReturnType
from ..errors import DeclarationError, make_already_declared_error, make_invalid_type_error
from ..utils import TypeOrEllipsis, is_ellipsis
from ._schema import GenericSchema, Schema

__all__ = ("DictSchema", "DictProps", "make_required", "optional",)


class optional:
    def __init__(self, key: Any) -> None:
        if is_ellipsis(key):
            raise TypeError(key)
        self._key = key

    @property
    def key(self) -> Any:
        return self._key

    def __repr__(self) -> str:
        return f"optional({self._key!r})"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and (self._key == other.key)

    def __hash__(self) -> int:
        return hash((self._key,))


class DictProps(Props):
    @property
    def keys(self) -> Nilable[Dict[Any, Tuple[GenericSchema, bool]]]:
        return self.get("keys")


class DictSchema(Schema[DictProps]):
    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        return visitor.visit_dict(self, **kwargs)

    def __call__(self, /, keys: Dict[Any, TypeOrEllipsis[GenericSchema]]) -> "DictSchema":
        if not isinstance(keys, dict):
            raise make_invalid_type_error(self, keys, (dict,))

        if self.props.keys is not Nil:
            raise make_already_declared_error(self)

        real_keys = {}
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
            if isinstance(key, optional):
                real_keys[key.key] = (val, True)
            else:
                real_keys[key] = (val, False)

        return self.__class__(self.props.update(keys=real_keys))

    def __getitem__(self, /, key: Any) -> GenericSchema:
        if (self.props.keys is Nil) or (key not in self.props.keys) or (is_ellipsis(key)):
            key_repr = "..." if is_ellipsis(key) else key
            raise KeyError(key_repr)
        return self.props.keys[key][0]

    def __add__(self, /, other: "DictSchema") -> "DictSchema":
        assert isinstance(other, Schema)
        self_keys = self.props.keys if (self.props.keys is not Nil) else {}
        other_keys = other.props.keys if (other.props.keys is not Nil) else {}
        merged_keys = {**self_keys, **other_keys}
        return self.__class__(self.props.update(keys=merged_keys))

    def keys(self) -> KeysView[Any]:
        if self.props.keys is Nil:
            return {}.keys()
        return self.props.keys.keys()


def make_required(schema: DictSchema, keys: Union[Set[str], List[str], None] = None) -> DictSchema:
    if not isinstance(schema, DictSchema):
        message = f"Inappropriate type of schema {schema!r} ({type(schema)!r})"
        raise DeclarationError(message)

    actual_keys_list = list(schema.keys())

    if not actual_keys_list:
        message = "DictSchema must not be empty"
        raise DeclarationError(message)
    else:
        for key in actual_keys_list:
            if is_ellipsis(key):
                message = "DictSchema must not be relaxed"
                raise DeclarationError(message)

    if keys:
        if not isinstance(keys, (set, list)):
            message = f"Inappropriate type of keys {keys!r} ({type(keys)!r})"
            raise DeclarationError(message)
        for key in keys:
            if key not in actual_keys_list:
                message = f"Nonexisting key {key!r}"
                raise DeclarationError(message)

    keys_to_be_required = list(keys) if keys else actual_keys_list

    updated_keys = {}
    props_keys = {} if (schema.props.keys is Nil) else schema.props.keys
    for key, (val, is_optional) in props_keys.items():
        updated_keys[key] = (val, False if key in keys_to_be_required else is_optional)

    return schema.__class__(schema.props.update(keys=updated_keys))
