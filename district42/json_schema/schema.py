import warnings
from copy import deepcopy

from ..errors import DeclarationError
from .types import (Any, AnyOf, Array, ArrayOf, Boolean, Enum, Null, Number,
                    Object, OneOf, SchemaType, String, Timestamp, Undefined)


class Schema:

    def ref(self, schema):
        return deepcopy(schema)

    def from_native(self, value):
        if value is None:
            return self.null

        datatype = type(value)
        if datatype is bool:
            return self.boolean(value)
        elif datatype is int:
            return self.integer(value)
        elif datatype is float:
            return self.float(value)
        elif datatype is str:
            return self.string(value)
        elif datatype is list:
            return self.array([self.from_native(elem) for elem in value])
        elif datatype is dict:
            return self.object({k: self.from_native(v) for k, v in value.items()})
        elif datatype is tuple:
            return self.enum(*value)

        raise DeclarationError('Unknown type "{}"'.format(datatype))

    @property
    def null(self):
        return Null()

    @property
    def boolean(self):
        return Boolean()

    @property
    def number(self):
        message = 'schema.number is deprecated, use schema.one_of(schema.integer, schema.float) instead'
        warnings.warn(message, DeprecationWarning, stacklevel=2)
        return Number()

    @property
    def integer(self):
        return Number().integer

    @property
    def float(self):
        return Number().float

    @property
    def string(self):
        return String()

    @property
    def timestamp(self):
        return Timestamp()

    @property
    def array(self):
        return Array()

    @property
    def array_of(self):
        message = 'schema.array_of is deprecated, use schema.array.of instead'
        warnings.warn(message, DeprecationWarning, stacklevel=2)
        return ArrayOf()

    @property
    def object(self):
        return Object()

    @property
    def any(self):
        return Any()

    @property
    def any_of(self):
        return AnyOf()

    @property
    def one_of(self):
        return OneOf()

    @property
    def enum(self):
        return Enum()

    @property
    def undefined(self):
        return Undefined()
