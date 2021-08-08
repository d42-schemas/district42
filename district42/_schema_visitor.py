from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Generic, TypeVar

if TYPE_CHECKING:
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

__all__ = ("SchemaVisitor", "SchemaVisitorReturnType",)

SchemaVisitorReturnType = TypeVar("SchemaVisitorReturnType")


class SchemaVisitor(ABC, Generic[SchemaVisitorReturnType]):
    @abstractmethod
    def visit_none(self, schema: "NoneSchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    @abstractmethod
    def visit_bool(self, schema: "BoolSchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    @abstractmethod
    def visit_int(self, schema: "IntSchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    @abstractmethod
    def visit_float(self, schema: "FloatSchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    @abstractmethod
    def visit_str(self, schema: "StrSchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    @abstractmethod
    def visit_list(self, schema: "ListSchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    @abstractmethod
    def visit_dict(self, schema: "DictSchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    @abstractmethod
    def visit_any(self, schema: "AnySchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    @abstractmethod
    def visit_const(self, schema: "ConstSchema", **kwargs: Any) -> SchemaVisitorReturnType:
        pass

    def __getattr__(self, name: Any) -> Any:
        raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")

    def __init_subclass__(cls, **kwargs: Any) -> None:
        if kwargs.get("extend", False) is not True:
            return
        parent = cls.__bases__[0]
        assert issubclass(parent, SchemaVisitor)
        for name, value in cls.__dict__.items():
            if callable(value) and not name.startswith("__"):
                setattr(parent, name, value)
