from argparse import Namespace
from .json_schema.schema import Schema as JsonSchema
from .json_schema.abstract_visitor import AbstractVisitor
from .json_schema.representor import Representor
from .json_schema.errors import DeclarationError
from .json_schema.types import *
from .json_schema.modifiers import *


json_schema = JsonSchema()
json_schema.AbstractVisitor = AbstractVisitor
json_schema.Representor = Representor
json_schema.DeclarationError = DeclarationError
json_schema.types = Namespace()
json_schema.modifiers = Namespace()

json_schema.types.SchemaType = SchemaType
json_schema.types.Null = Null
json_schema.types.Boolean = Boolean
json_schema.types.Number = Number
json_schema.types.Integer = Integer
json_schema.types.Float = Float
json_schema.types.String = String
json_schema.types.Array = Array
json_schema.types.ArrayOf = ArrayOf
json_schema.types.Object = Object
json_schema.types.Any = Any
json_schema.types.AnyOf = AnyOf
json_schema.types.OneOf = OneOf
json_schema.types.Enum = Enum
json_schema.types.Undefined = Undefined

json_schema.modifiers.Nullable = Nullable
json_schema.modifiers.Valuable = Valuable
json_schema.modifiers.Comparable = Comparable
json_schema.modifiers.Subscriptable = Subscriptable
json_schema.modifiers.Emptyable = Emptyable
