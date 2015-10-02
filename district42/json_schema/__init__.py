from .representor import Representor
from .types import SchemaType


SchemaType.__repr__ = lambda self, *args, **kwargs: self.accept(Representor())
