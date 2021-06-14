from typing import Any

from ._props import Props
from ._schema_facade import SchemaFacade
from ._schema_visitor import SchemaVisitor
from ._version import version
from .representor import Representor
from .types import GenericSchema, Schema

__version__ = version
__all__ = ("schema", "GenericSchema", "Props", "SchemaVisitor",)


schema = SchemaFacade()
_representor = Representor()


def represent(self: GenericSchema, **kwargs: Any) -> str:
    return self.__accept__(_representor, **kwargs)


Schema.__override__("__repr__", represent)
