import warnings

from ..errors import DeclarationError
from ..helpers import check_type


class Nullable:

    @property
    def nullable(self):
        message = '.nullable is deprecated, use "{} | schema.null" instead'.format(self)
        warnings.warn(message, DeprecationWarning, stacklevel=2)
        self._params['nullable'] = True
        return self


class Valuable:

    def val(self, value):
        error = check_type(value, self._valuable_types)
        if error:
            raise DeclarationError(error)
        self._params['value'] = value
        return self

    def __call__(self, value):
        return self.val(value)


class Comparable:
    
    def min(self, value):
        self._params['min_value'] = value
        return self

    def max(self, value):
        self._params['max_value'] = value
        return self

    def between(self, min_value, max_value):
        self._params['min_value'] = min_value
        self._params['max_value'] = max_value
        return self


class Subscriptable:
    
    def length(self, *args):
        if not (1 <= len(args) <= 2):
            raise DeclarationError()

        if len(args) == 1:
            self._params['length'] = args[0]
        else:
            self._params['min_length'] = args[0]
            self._params['max_length'] = args[1]

        return self

    def min_length(self, value):
        self._params['min_length'] = value
        return self

    def max_length(self, value):
        self._params['max_length'] = value
        return self


class Emptyable:

    @property
    def empty(self):
        self._params['empty'] = True
        self._params['length'] = 0
        return self

    @property
    def non_empty(self):
        self._params['empty'] = False
        self._params['min_length'] = 1
        return self
