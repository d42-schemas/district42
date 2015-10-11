import re
from copy import deepcopy
from .modifiers import *


class SchemaType:

  def __init__(self):
    self._params = {}

  def __copy__(self):
    cls = self.__class__
    clone = cls.__new__(cls)
    clone.__dict__.update(self.__dict__)
    return clone

  def __deepcopy__(self, memo):
    cls = self.__class__
    clone = cls.__new__(cls)
    memo[id(self)] = clone
    for attr, val in self.__dict__.items():
      setattr(clone, attr, deepcopy(val, memo))
    return clone

  @property
  def required(self):
    self._params['required'] = True
    return self

  @property
  def optional(self):
    self._params['required'] = False
    return self

  def example(self, example):
    self._params['examples'] = [example]
    return self

  def examples(self, example1, example2, *examples):
    self._params['examples'] = [example1, example2] + list(examples)
    return self

  def accept(self, visitor, *args, **kwargs):
    method = re.sub('([A-Z]+)', r'_\1', self.__class__.__name__).lower()
    return getattr(visitor, 'visit' + method)(self, *args, **kwargs)


class Null(SchemaType):
  pass


class Boolean(Nullable, Valuable, SchemaType):
  
  _valuable_types = [bool]


class Integer(Nullable, Valuable, Comparable, SchemaType):

  _valuable_types = [int]

  @property
  def positive(self):
    self._params['positive'] = True
    self._params['min_value'] = 1
    return self

  @property
  def negative(self):
    self._params['negative'] = True
    self._params['max_value'] = -1
    return self

  @property
  def zero(self):
    self._params['zero'] = True
    self._params['value'] = 0
    return self

  def multiple(self, base):
    self._params['multiple'] = base
    return self


class Float(Nullable, Valuable, Comparable, SchemaType):

  _valuable_types = [float]

  @property
  def positive(self):
    self._params['positive'] = True
    self._params['min_value'] = 1.0
    return self

  @property
  def negative(self):
    self._params['negative'] = True
    self._params['max_value'] = -1.0
    return self

  @property
  def zero(self):
    self._params['zero'] = True
    self._params['value'] = 0.0
    return self


class Number(Nullable, Valuable, Comparable, SchemaType):

  _valuable_types = [int, float]

  @property
  def integer(self):
    return Integer()

  @property
  def float(self):
    return Float()

  @property
  def positive(self):
    self._params['positive'] = True
    self._params['min_value'] = 1
    return self

  @property
  def negative(self):
    self._params['negative'] = True
    self._params['max_value'] = -1
    return self

  @property
  def zero(self):
    self._params['zero'] = True
    self._params['value'] = 0
    return self

  def multiple(self, base):
    self._params['multiple'] = base
    return self


class String(Nullable, Valuable, Subscriptable, Emptyable, SchemaType):

  _valuable_types = [str]

  def pattern(self, pattern):
    self._params['pattern'] = pattern
    return self

  @property
  def alphabetic(self):
    self._params['alphabetic'] = True
    return self

  @property
  def numeric(self):
    self._params['numeric'] = True
    return self

  @property
  def alpha_num(self):
    self._params['alpha_num'] = True
    return self

  @property
  def lowercase(self):
    self._params['lowercase'] = True
    return self

  @property
  def uppercase(self):
    self._params['uppercase'] = True
    return self


class Array(Nullable, Subscriptable, Emptyable, SchemaType):
  
  def __call__(self, items):
    self._params['items'] = items
    return self

  def contains(self, item):
    self._params['contains'] = item
    return self

  def contains_one(self, item):
    self._params['contains_one'] = item
    return self

  def contains_many(self, item):
    self._params['contains_many'] = item
    return self


class ArrayOf(Nullable, Subscriptable, SchemaType):
  
  def __call__(self, items_schema):
    self._params['items_schema'] = items_schema
    return self


class Object(Nullable, Subscriptable, Emptyable, SchemaType):

  def __init__(self):
    super().__init__()
    self._params['keys'] = {}
  
  def __call__(self, keys):
    self._params['keys'] = self.__roll_out(keys)
    return self

  def __add__(self, keys):
    return self.extend(keys)

  def __contains__(self, composite_key):
    parts = composite_key.split('.')
    if len(parts) == 1:
      return parts[0] in self._params['keys']
    return parts[0] in self._params['keys'] and '.'.join(parts[1:]) in self._params['keys'][parts[0]]

  def __getitem__(self, composite_key):
    parts = composite_key.split('.')
    if len(parts) == 1:
      return self._params['keys'][parts[0]]
    return self._params['keys'][parts[0]]['.'.join(parts[1:])]

  def __roll_out(self, keys):
    new_keys = {}
    for composite_key, val in keys.items():
      parts = composite_key.split('.')
      key = parts[0]
      if key[-1] == '?':
        key = key[:-1]
        val._params['required'] = False
      if len(parts) == 1:
        new_keys[key] = deepcopy(val)
      else:
        comp_key = '.'.join(parts[1:])
        if key not in new_keys:
          new_keys[key] = self.__class__()({comp_key: val})
        else:
          new_keys[key]._params['keys'].update(self.__roll_out({comp_key: val}))
    return new_keys

  def extend(self, keys):
    clone = deepcopy(self)
    clone._params['keys'].update(self.__roll_out(keys))
    return clone


class Any(Nullable, SchemaType):
  pass


class AnyOf(Nullable, SchemaType):

  def __call__(self, option1, option2, *options):
    self._params['options'] = [option1, option2] + list(options)
    return self


class OneOf(Nullable, SchemaType):

  def __call__(self, option1, option2, *options):
    self._params['options'] = [option1, option2] + list(options)
    return self


class Enum(Nullable, SchemaType):

  def __call__(self, enumerator1, enumerator2, *enumerators):
    self._params['enumerators'] = [enumerator1, enumerator2] + list(enumerators)
    return self


class Undefined(SchemaType):
  pass
