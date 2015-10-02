from .json_schema.schema import Schema as JsonSchema
from .json_schema.abstract_visitor import AbstractVisitor
from .json_schema.representor import Representor
from .json_schema.errors import DeclarationError


json_schema = JsonSchema()
json_schema.AbstractVisitor = AbstractVisitor
json_schema.Representor = Representor
json_schema.DeclarationError = DeclarationError
