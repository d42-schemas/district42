import unittest
import district42.json_schema as schema


class TestRepresentation(unittest.TestCase):

  def assertRepr(self, _schema, _repr):
    return self.assertEqual(repr(_schema), _repr)
  
  def test_null_type_repr(self):
    self.assertRepr(schema.null, 'schema.null')

  def test_boolean_type_repr(self):
    self.assertRepr(schema.boolean,          'schema.boolean')
    self.assertRepr(schema.boolean(True),    'schema.boolean(True)')
    self.assertRepr(schema.boolean.nullable, 'schema.boolean.nullable')

  def test_number_type_repr(self):
    self.assertRepr(schema.number,               'schema.number')
    self.assertRepr(schema.number(42),           'schema.number(42)')
    self.assertRepr(schema.number(3.14),         'schema.number(3.14)')
    self.assertRepr(schema.number.min(0),        'schema.number.min(0)')
    self.assertRepr(schema.number.max(1),        'schema.number.max(1)')
    self.assertRepr(schema.number.between(0, 1), 'schema.number.between(0, 1)')
    self.assertRepr(schema.number.positive,      'schema.number.positive')
    self.assertRepr(schema.number.negative,      'schema.number.negative')
    self.assertRepr(schema.number.zero,          'schema.number.zero')
    self.assertRepr(schema.number.multiple(5),   'schema.number.multiple(5)')
    self.assertRepr(schema.number.nullable,      'schema.number.nullable')

  def test_integer_type_repr(self):
    self.assertRepr(schema.integer,               'schema.integer')
    self.assertRepr(schema.integer(42),           'schema.integer(42)')
    self.assertRepr(schema.integer.min(0),        'schema.integer.min(0)')
    self.assertRepr(schema.integer.max(1),        'schema.integer.max(1)')
    self.assertRepr(schema.integer.between(0, 1), 'schema.integer.between(0, 1)')
    self.assertRepr(schema.integer.positive,      'schema.integer.positive')
    self.assertRepr(schema.integer.negative,      'schema.integer.negative')
    self.assertRepr(schema.integer.zero,          'schema.integer.zero')
    self.assertRepr(schema.integer.multiple(5),   'schema.integer.multiple(5)')
    self.assertRepr(schema.integer.nullable,      'schema.integer.nullable')

  def test_float_type_repr(self):
    self.assertRepr(schema.float,                   'schema.float')
    self.assertRepr(schema.float(3.14),             'schema.float(3.14)')
    self.assertRepr(schema.float.min(0.0),          'schema.float.min(0.0)')
    self.assertRepr(schema.float.max(1.0),          'schema.float.max(1.0)')
    self.assertRepr(schema.float.between(0.0, 1.0), 'schema.float.between(0.0, 1.0)')
    self.assertRepr(schema.float.positive,          'schema.float.positive')
    self.assertRepr(schema.float.negative,          'schema.float.negative')
    self.assertRepr(schema.float.zero,              'schema.float.zero')
    self.assertRepr(schema.float.nullable,          'schema.float.nullable')

  def test_string_type_repr(self):
    self.assertRepr(schema.string,                      'schema.string')
    self.assertRepr(schema.string('banana'),            "schema.string('banana')")
    self.assertRepr(schema.string.length(32),           'schema.string.length(32)')
    self.assertRepr(schema.string.length(1, 64),        'schema.string.length(1, 64)')
    self.assertRepr(schema.string.empty,                'schema.string.empty')
    self.assertRepr(schema.string.pattern(r'[0-9\-_]'), "schema.string.pattern(r'[0-9\-_]')")
    self.assertRepr(schema.string.alphabetic,           'schema.string.alphabetic')
    self.assertRepr(schema.string.numeric,              'schema.string.numeric')
    self.assertRepr(schema.string.alpha_num,            'schema.string.alpha_num')
    self.assertRepr(schema.string.lowercase,            'schema.string.lowercase')
    self.assertRepr(schema.string.uppercase,            'schema.string.uppercase')
    self.assertRepr(schema.string.nullable,             'schema.string.nullable')

  def test_array_type_repr(self):
    self.assertRepr(schema.array,              'schema.array')
    self.assertRepr(schema.array.nullable,     'schema.array.nullable')
    self.assertRepr(schema.array([]),          'schema.array([])')
    self.assertRepr(schema.array.length(10),   'schema.array.length(10)')
    self.assertRepr(schema.array.length(1, 2), 'schema.array.length(1, 2)')
    self.assertRepr(schema.array.empty,        'schema.array.empty')

    self.assertRepr(schema.array([schema.integer(0), schema.integer(1)]),
                   'schema.array([schema.integer(0), schema.integer(1)])')

    self.assertRepr(schema.array.contains(schema.integer(42)),
                   'schema.array.contains(schema.integer(42))')
    self.assertRepr(schema.array.contains_one(schema.boolean),
                   'schema.array.contains_one(schema.boolean)')
    self.assertRepr(schema.array.contains_many(schema.string('banana')),
                   "schema.array.contains_many(schema.string('banana'))")

    self.assertRepr(
      schema.array.contains(schema.object({
        'id': schema.integer(1)
      })),
      "schema.array.contains(schema.object({" + "\n" +
      "  'id': schema.integer(1)" + "\n" +
      "}))"
    )

    self.assertRepr(
      schema.array([
        schema.integer(1),
        schema.integer(2),
        schema.integer(3)
      ]),
      "schema.array([" + "\n" +
      "  schema.integer(1)," + "\n" +
      "  schema.integer(2)," + "\n" +
      "  schema.integer(3)" + "\n" +
      "])"
    )
    
    self.assertRepr(
      schema.array([
        schema.integer(1),
        schema.integer(2),
        schema.object({
          'id': schema.string.numeric
        })
      ]),
      "schema.array([" + "\n" +
      "  schema.integer(1)," + "\n" +
      "  schema.integer(2)," + "\n" +
      "  schema.object({" + "\n" +
      "    'id': schema.string.numeric" + "\n" +
      "  })" + "\n" +
      "])"
    )

    self.assertRepr(
      schema.object({
        'items': schema.array([schema.object({
          'id': schema.string.numeric
        })])
      }),
      "schema.object({" + "\n" +
      "  'items': schema.array([schema.object({" + "\n" +
      "    'id': schema.string.numeric" + "\n" +
      "  })])" + "\n" +
      "})"
    )
  
  def test_array_of_type_repr(self):
    self.assertRepr(schema.array_of(schema.number),
                   'schema.array_of(schema.number)')

    self.assertRepr(schema.array_of(schema.boolean).nullable,
                   'schema.array_of(schema.boolean).nullable')

    self.assertRepr(schema.array_of(schema.number).length(2),
                   'schema.array_of(schema.number).length(2)')

    self.assertRepr(schema.array_of(schema.number).length(1, 10),
                   'schema.array_of(schema.number).length(1, 10)')

    self.assertRepr(
      schema.array_of(schema.object({
        'id': schema.string.numeric
      })),
      "schema.array_of(schema.object({" + "\n" +
      "  'id': schema.string.numeric" + "\n" +
      "}))"
    )

  def test_object_type_repr(self):
    self.assertRepr(schema.object,              'schema.object')
    self.assertRepr(schema.object.nullable,     'schema.object.nullable')
    self.assertRepr(schema.object.length(1),    'schema.object.length(1)')
    self.assertRepr(schema.object.length(0, 1), 'schema.object.length(0, 1)')
    self.assertRepr(schema.object.empty,        'schema.object.empty')
    
    self.assertRepr(
      schema.object({
        'id': schema.integer.positive
      }),
      "schema.object({" + "\n" +
      "  'id': schema.integer.positive" + "\n" +
      "})"
    )

    self.assertRepr(
      schema.object({
        'attrs': schema.object({
          'height': schema.float,
          'width': schema.float
        }),
        'id': schema.integer.positive
      }),
      "schema.object({" + "\n" +
      "  'attrs': schema.object({" + "\n" +
      "    'height': schema.float," + "\n" +
      "    'width': schema.float" + "\n" +
      "  })," + "\n" +
      "  'id': schema.integer.positive" + "\n" +
      "})"
    )

  def test_any_type_repr(self):
    self.assertRepr(schema.any,          'schema.any')
    self.assertRepr(schema.any.nullable, 'schema.any.nullable')

  def test_any_of_type_repr(self):
    self.assertRepr(schema.any_of(schema.integer, schema.string.numeric),
                   'schema.any_of(schema.integer, schema.string.numeric)')

    self.assertRepr(schema.any_of(schema.integer(0), schema.integer(1)).nullable,
                   'schema.any_of(schema.integer(0), schema.integer(1)).nullable')

  def test_one_of_type_repr(self):
    self.assertRepr(schema.one_of(schema.integer, schema.string.numeric),
                   'schema.one_of(schema.integer, schema.string.numeric)')

    self.assertRepr(schema.one_of(schema.integer(0), schema.integer(1)).nullable,
                   'schema.one_of(schema.integer(0), schema.integer(1)).nullable')

  def test_enum_type_repr(self):
    self.assertRepr(schema.enum(1, 2, 3),       'schema.enum(1, 2, 3)')
    self.assertRepr(schema.enum('a', 'b', 'c'), "schema.enum('a', 'b', 'c')")
    self.assertRepr(schema.enum(0, 1).nullable, 'schema.enum(0, 1).nullable')

  def test_undefined_type_repr(self):
    self.assertRepr(schema.undefined, 'schema.undefined')


if __name__ == '__main__':
  unittest.main()
