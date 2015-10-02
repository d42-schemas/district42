from .errors import DeclarationError


class Nullable:

  @property
  def nullable(self):
    self._params['nullable'] = True
    return self


class Valuable:

  def __call__(self, value):
    if type(value) not in self._valuable_types: 
      raise DeclarationError()
    self._params['value'] = value
    return self


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


class Emptyable:

  @property
  def empty(self):
    self._params['empty'] = True
    self._params['length'] = 0
    return self
