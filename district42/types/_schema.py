from abc import ABC, abstractmethod
from typing import Any, Generic, cast

from niltype import Nil, Nilable

from .._props import PropsType
from .._schema_visitor import SchemaVisitor
from .._schema_visitor import SchemaVisitorReturnType as ReturnType

__all__ = ("Schema", "GenericSchema",)


class Schema(ABC, Generic[PropsType]):
    def __init__(self, props: Nilable[PropsType] = Nil) -> None:
        props_type = self.__orig_bases__[0].__args__[0]  # type: ignore
        self._props = cast(PropsType, props_type()) if props is Nil else props

    @property
    def props(self) -> PropsType:
        return self._props

    @abstractmethod
    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        pass

    @classmethod
    def __override__(cls, method: str, fn: Any) -> None:
        setattr(cls, method, fn)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.props!r})"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and (self.props == other.props)

    def __or__(self, other: Any) -> Any:
        raise AttributeError("Schema has no attribute '__or__'")

    def __invert__(self) -> Any:
        raise AttributeError("Schema has no attribute '__invert__'")

    def __mod__(self, other: Any) -> Any:
        raise AttributeError("Schema has no attribute '__mod__'")


GenericSchema = Schema[Any]
