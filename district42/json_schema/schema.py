from copy import deepcopy
from .types import *


class Schema:

  def ref(self, schema):
    return deepcopy(schema)

  @property
  def null(self):
    return Null()

  @property
  def boolean(self):
    return Boolean()

  @property
  def number(self):
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
  def array(self):
    return Array()

  @property
  def array_of(self):
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
