from typing import Any

from ._from_native import from_native
from ._props import Props
from ._schema_facade import SchemaFacade
from ._schema_visitor import SchemaVisitor
from ._version import version
from .representor import Representor
from .types import AnySchema, GenericSchema, Schema

__version__ = version
__all__ = ("schema", "GenericSchema", "Props", "SchemaVisitor", "from_native",)


schema = SchemaFacade()
_representor = Representor()


def represent(self: GenericSchema, **kwargs: Any) -> str:
    return self.__accept__(_representor, **kwargs)


def union(self: GenericSchema, other: Any) -> AnySchema:
    return schema.any(self, other)


Schema.__override__("__repr__", represent)
Schema.__override__("__or__", union)
