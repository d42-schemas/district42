from .types import Array, Object
from .abstract_visitor import AbstractVisitor


class Representor(AbstractVisitor):

  def __is_indentable(self, schema):
    return type(schema) in [Object, Array]

  def __get_array_items(self, items, indent):
    for item in items:
      if self.__is_indentable(item):
        yield item.accept(self, indent)
      else:
        yield item.accept(self)

  def __get_object_keys(self, items, indent):
    keys = []
    for key, val in items:
      if self.__is_indentable(val):
        _repr = val.accept(self, indent)
      else:
        _repr = val.accept(self)
      if 'required' in val._params and not val._params['required']:
        key += '?'
      keys.append("{}'{}': {}".format(' ' * indent, key, _repr))
    return keys

  def __to_iso_format(self, timestamp):
    return timestamp.datetime.isoformat()

  def visit_null(self, schema):
    res = 'schema.null'
    return res

  def visit_boolean(self, schema):
    res = 'schema.boolean'

    if 'value' in schema._params:
      res += '({})'.format(schema._params['value'])

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_number(self, schema):
    if 'integer' in schema._params and schema._params['integer']:
      res = 'schema.integer'
    elif 'float' in schema._params and schema._params['float']:
      res = 'schema.float'
    else:
      res = 'schema.number'

    if 'zero' in schema._params:
      res += '.zero'
    elif 'value' in schema._params:
      res += '({})'.format(schema._params['value'])
    elif 'unsigned' in schema._params:
      res += '.unsigned'
    elif 'positive' in schema._params:
      res += '.positive' if schema._params['positive'] else '.non_positive'
    elif 'negative' in schema._params:
      res += '.negative' if schema._params['negative'] else '.non_negative'
    elif 'min_value' in schema._params and 'max_value' in schema._params:
      res += '.between({}, {})'.format(schema._params['min_value'], schema._params['max_value'])
    elif 'min_value' in schema._params:
      res += '.min({})'.format(schema._params['min_value'])
    elif 'max_value' in schema._params:
      res += '.max({})'.format(schema._params['max_value'])

    if 'multiple' in schema._params:
      res += '.multiple({})'.format(schema._params['multiple'])

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_string(self, schema):
    res = 'schema.string'

    if 'value' in schema._params:
      res += '({})'.format(repr(schema._params['value']))

    if 'pattern' in schema._params:
      res += '.pattern(r\'{}\')'.format(schema._params['pattern'])
    elif 'uri' in schema._params:
      res += '.uri'

    if 'alphabetic' in schema._params:
      res += '.alphabetic'
    elif 'numeric' in schema._params:
      res += '.numeric'
    elif 'alpha_num' in schema._params:
      res += '.alpha_num'

    if 'lowercase' in schema._params:
      res += '.lowercase'
    elif 'uppercase' in schema._params:
      res += '.uppercase'

    if 'empty' in schema._params:
      res += '.empty' if schema._params['empty'] else '.non_empty'
    elif 'length' in schema._params:
      res += '.length({})'.format(schema._params['length'])
    elif 'min_length' in schema._params and 'max_length' in schema._params:
      res += '.length({}, {})'.format(schema._params['min_length'], schema._params['max_length'])
    elif 'min_length' in schema._params:
      res += '.min_length({})'.format(schema._params['min_length'])
    elif 'max_length' in schema._params:
      res += '.max_length({})'.format(schema._params['max_length'])

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_timestamp(self, schema):
    res = 'schema.timestamp'

    if 'value' in schema._params:
      res += '({})'.format(repr(self.__to_iso_format(schema._params['value'])))

    if 'iso' in schema._params:
      res += '.iso'
    elif 'format' in schema._params:
      res += '.format({})'.format(repr(schema._params['format']))

    if 'min_value' in schema._params and 'max_value' in schema._params:
      res += '.between({}, {})'.format(repr(self.__to_iso_format(schema._params['min_value'])),
                                       repr(self.__to_iso_format(schema._params['max_value'])))
    elif 'min_value' in schema._params:
      res += '.min({})'.format(repr(self.__to_iso_format(schema._params['min_value'])))
    elif 'max_value' in schema._params:
      res += '.max({})'.format(repr(self.__to_iso_format(schema._params['max_value'])))

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_array(self, schema, indent = 0):
    res = 'schema.array'
 
    if 'items' in schema._params:
      items = schema._params['items']
      if len(items) <= 2:
        res += '([{}])'.format(', '.join(self.__get_array_items(items, indent)))
      else:
        separator = ',\n' + ' ' * (indent + 2)
        res += '([\n  {}\n])'.format(separator.join(self.__get_array_items(items, indent + 2)))
    elif 'contains' in schema._params:
      res += '.contains'
      item = schema._params['contains']
      if self.__is_indentable(item):
        res += '({})'.format(item.accept(self, indent))
      else:
        res += '({})'.format(item.accept(self))
    elif 'contains_one' in schema._params:
      res += '.contains_one'
      item = schema._params['contains_one']
      if self.__is_indentable(item):
        res += '({})'.format(item.accept(self, indent))
      else:
        res += '({})'.format(item.accept(self))
    elif 'contains_many' in schema._params:
      res += '.contains_many'
      item = schema._params['contains_many']
      if self.__is_indentable(item):
        res += '({})'.format(item.accept(self, indent))
      else:
        res += '({})'.format(item.accept(self))

    if 'empty' in schema._params:
      res += '.empty' if schema._params['empty'] else '.non_empty'
    elif 'length' in schema._params:
      res += '.length({})'.format(schema._params['length'])
    elif 'min_length' in schema._params and 'max_length' in schema._params:
      res += '.length({}, {})'.format(schema._params['min_length'], schema._params['max_length'])
    elif 'min_length' in schema._params:
      res += '.min_length({})'.format(schema._params['min_length'])
    elif 'max_length' in schema._params:
      res += '.max_length({})'.format(schema._params['max_length'])

    if 'unique' in schema._params:
      res += '.unique(<predicate>)' if 'predicate' in schema._params else '.unique'

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_array_of(self, schema, indent = 0):
    res = 'schema.array_of'

    items_schema = schema._params['items_schema']
    if self.__is_indentable(items_schema):
      res += '({})'.format(items_schema.accept(self, indent))
    else:
      res += '({})'.format(items_schema.accept(self))

    if 'empty' in schema._params:
      res += '.empty' if schema._params['empty'] else '.non_empty'
    elif 'length' in schema._params:
      res += '.length({})'.format(schema._params['length'])
    elif 'min_length' in schema._params and 'max_length' in schema._params:
      res += '.length({}, {})'.format(schema._params['min_length'], schema._params['max_length'])
    elif 'min_length' in schema._params:
      res += '.min_length({})'.format(schema._params['min_length'])
    elif 'max_length' in schema._params:
      res += '.max_length({})'.format(schema._params['max_length'])

    if 'unique' in schema._params:
      res += '.unique(<predicate>)' if 'predicate' in schema._params else '.unique'

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_object(self, schema, indent = 0):
    res = 'schema.object'

    if 'keys' in schema._params:
      if len(schema._params['keys']) > 0:
        res += '({\n'
        sorted_items = sorted(schema._params['keys'].items())
        keys = self.__get_object_keys(sorted_items, indent + 2)
        res += ',\n'.join(keys) + '\n' + (' ' * indent) + '})'
      else:
        res += '({})'

    if 'empty' in schema._params:
      res += '.empty' if schema._params['empty'] else '.non_empty'
    elif 'length' in schema._params:
      res += '.length({})'.format(schema._params['length'])
    elif 'min_length' in schema._params and 'max_length' in schema._params:
      res += '.length({}, {})'.format(schema._params['min_length'], schema._params['max_length'])
    elif 'min_length' in schema._params:
      res += '.min_length({})'.format(schema._params['min_length'])
    elif 'max_length' in schema._params:
      res += '.max_length({})'.format(schema._params['max_length'])

    if 'strict' in schema._params:
      res += '.strict'

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_any(self, schema):
    res = 'schema.any'

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_any_of(self, schema):
    res = 'schema.any_of'

    res += '({})'.format(', '.join(map(repr, schema._params['options'])))

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_one_of(self, schema, indent = 0):
    res = 'schema.one_of'

    res += '({})'.format(', '.join(map(repr, schema._params['options'])))

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_enum(self, schema):
    res = 'schema.enum'

    res += '({})'.format(', '.join(map(repr, schema._params['enumerators'])))

    if 'nullable' in schema._params:
      res += '.nullable'

    return res

  def visit_undefined(self, schema):
    res = 'schema.undefined'
    return res
