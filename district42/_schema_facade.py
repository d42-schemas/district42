from typing import Any

from .types import (
    AnySchema,
    BoolSchema,
    ConstSchema,
    DictSchema,
    FloatSchema,
    IntSchema,
    ListSchema,
    NoneSchema,
    StrSchema,
)

__all__ = ("SchemaFacade",)


class SchemaFacade:
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
        return ConstSchema()

    def __getattr__(self, name: Any) -> Any:
        raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")
