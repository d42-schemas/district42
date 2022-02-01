import warnings
from typing import Any

from .types import (
    AnySchema,
    BoolSchema,
    BytesSchema,
    ConstSchema,
    DictSchema,
    FloatSchema,
    GenericSchema,
    IntSchema,
    ListSchema,
    NoneSchema,
    StrSchema,
    TypeAliasProps,
    TypeAliasSchema,
)

__all__ = ("SchemaFacade",)


class SchemaFacade:
    def alias(self, /, name: str, type_: GenericSchema) -> TypeAliasSchema:
        props = TypeAliasProps()
        return TypeAliasSchema(props.update(name=name, type=type_))

    @property
    def none(self) -> NoneSchema:
        return NoneSchema()

    @property
    def bool(self) -> BoolSchema:
        return BoolSchema()

    @property
    def int(self) -> IntSchema:
        return IntSchema()

    @property
    def float(self) -> FloatSchema:
        return FloatSchema()

    @property
    def str(self) -> StrSchema:
        return StrSchema()

    @property
    def list(self) -> ListSchema:
        return ListSchema()

    @property
    def dict(self) -> DictSchema:
        return DictSchema()

    @property
    def any(self) -> AnySchema:
        return AnySchema()

    @property
    def const(self) -> ConstSchema:
        warnings.warn("Deprecated: 'schema.const' may be removed in the future", FutureWarning)
        return ConstSchema()

    @property
    def bytes(self) -> BytesSchema:
        return BytesSchema()

    def __getattr__(self, name: Any) -> Any:
        raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")
