import re
from copy import deepcopy

import delorean

from .errors import DeclarationError
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

  def __check_type__(self, value, expected_types):
    for expected_type in expected_types:
      if isinstance(value, expected_type):
        return expected_type
    if len(expected_types) == 2:
      message = 'Value "{value}" must be an instance of {type1} or {type2}, instance of {actual_type} given'
    elif len(expected_types) == 1:
      message = 'Value "{value}" must be an instance of {type1}, instance of {actual_type} given'
    else:
      message = 'Value "{value}" must be an instance of {types}, instance of {actual_type} given'
    raise DeclarationError(message.format(
      value=value,
      type1=expected_types[0],
      type2=expected_types[-1],
      types=tuple(expected_types),
      actual_type=type(value)
    ))

  def __check_types__(self, values, expected_types):
    return all(self.__check_type__(value, expected_types) for value in values)

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


class Number(Nullable, Valuable, Comparable, SchemaType):

  _valuable_types = [int, float]

  @property
  def integer(self):
    self._params['integer'] = True
    self._valuable_types = [int]
    return self

  @property
  def float(self):
    self._params['float'] = True
    self._valuable_types = [float]
    return self

  @property
  def positive(self):
    self._params['positive'] = True
    if 'float' in self._params and self._params['float']:
      self._params['min_value'] = 1.0
    else:
      self._params['min_value'] = 1
    return self

  @property
  def non_positive(self):
    self._params['positive'] = False
    if 'float' in self._params and self._params['float']:
      self._params['max_value'] = 0.0
    else:
      self._params['max_value'] = 0
    return self

  @property
  def negative(self):
    self._params['negative'] = True
    if 'float' in self._params and self._params['float']:
      self._params['max_value'] = -1.0
    else:
      self._params['max_value'] = -1
    return self

  @property
  def non_negative(self):
    self._params['negative'] = False
    if 'float' in self._params and self._params['float']:
      self._params['min_value'] = 0.0
    else:
      self._params['min_value'] = 0
    return self

  @property
  def zero(self):
    self._params['zero'] = True
    if 'float' in self._params and self._params['float']:
      self._params['value'] = 0.0
    else:
      self._params['value'] = 0
    return self

  @property
  def unsigned(self):
    self._params['unsigned'] = True
    return self.non_negative

  def multiple(self, base):
    self._params['multiple'] = base
    return self


class String(Nullable, Valuable, Subscriptable, Emptyable, SchemaType):

  _valuable_types = [str]

  def pattern(self, pattern):
    self._params['pattern'] = pattern
    return self

  @property
  def uri(self):
    self._params['uri'] = True
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


class Timestamp(Nullable, Valuable, Comparable, SchemaType):

  _valuable_types = [str]

  def __call__(self, value):
    self._params['value'] = delorean.parse(value)
    return self

  def min(self, value):
    self._params['min_value'] = delorean.parse(value)
    return self

  def max(self, value):
    self._params['max_value'] = delorean.parse(value)
    return self

  def between(self, min_value, max_value):
    self._params['min_value'] = delorean.parse(min_value)
    self._params['max_value'] = delorean.parse(max_value)
    return self

  @property
  def iso(self):
    self._params['iso'] = True
    return self

  def format(self, timestamp_format):
    self._params['format'] = timestamp_format
    return self


class Array(Nullable, Subscriptable, Emptyable, SchemaType):

  def __call__(self, predicate_or_items):
    if 'unique' in self._params:
      self._params['predicate'] = predicate_or_items
    else:
      super().__check_type__(predicate_or_items, [list])
      super().__check_types__(predicate_or_items, [SchemaType])
      self._params['items'] = predicate_or_items
    return self

  @property
  def unique(self):
    self._params['unique'] = True
    return self

  def contains(self, item):
    super().__check_type__(item, [SchemaType])
    self._params['contains'] = item
    return self

  def contains_one(self, item):
    super().__check_type__(item, [SchemaType])
    self._params['contains_one'] = item
    return self

  def contains_many(self, item):
    super().__check_type__(item, [SchemaType])
    self._params['contains_many'] = item
    return self


class ArrayOf(Nullable, Subscriptable, Emptyable, SchemaType):
  
  def __call__(self, predicate_or_items_schema):
    if 'unique' in self._params:
      self._params['predicate'] = predicate_or_items_schema
    else:
      super().__check_type__(predicate_or_items_schema, [SchemaType])
      self._params['items_schema'] = predicate_or_items_schema
    return self

  @property
  def unique(self):
    self._params['unique'] = True
    return self


class Object(Nullable, Subscriptable, Emptyable, SchemaType):

  @property
  def strict(self):
    self._params['strict'] = True
    return self

  def __call__(self, keys):
    super().__check_type__(keys, [dict])
    self._params['keys'] = self.__roll_out(keys)
    return self

  def __add__(self, keys):
    return self.extend(keys)

  def items(self):
    return self._params['keys'].items()

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
      super().__check_type__(val, [SchemaType])
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
    super().__check_type__(keys, [SchemaType, dict])
    clone = deepcopy(self)
    clone._params['keys'].update(self.__roll_out(keys))
    return clone


class Any(Nullable, SchemaType):
  pass


class AnyOf(Nullable, SchemaType):

  def __call__(self, option1, option2, *options):
    all_options = [option1, option2] + list(options)
    super().__check_types__(all_options, [SchemaType])
    self._params['options'] = all_options
    return self


class OneOf(Nullable, SchemaType):

  def __call__(self, option1, option2, *options):
    all_options = [option1, option2] + list(options)
    super().__check_types__(all_options, [SchemaType])
    self._params['options'] = all_options
    return self


class Enum(Nullable, SchemaType):

  def __call__(self, enumerator1, enumerator2, *enumerators):
    self._params['enumerators'] = [enumerator1, enumerator2] + list(enumerators)
    return self


class Undefined(SchemaType):
  pass
