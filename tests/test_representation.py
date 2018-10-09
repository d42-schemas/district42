import unittest
import warnings

from district42 import json_schema as schema

from .representation_testcase import RepresentationTestCase


class TestRepresentation(RepresentationTestCase):

    def test_null_type_representation(self):
        self.assertRepr(schema.null, 'schema.null')

    def test_boolean_type_representation(self):
        self.assertRepr(schema.boolean,          'schema.boolean')
        self.assertRepr(schema.boolean(True),    'schema.boolean(True)')

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.boolean.nullable, 'schema.boolean.nullable')

    def test_number_type_representation(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.number, 'schema.number')
            self.assertRepr(schema.number(42), 'schema.number(42)')
            self.assertRepr(schema.number(3.14), 'schema.number(3.14)')

    def test_integer_type_representation(self):
        self.assertRepr(schema.integer,               'schema.integer')
        self.assertRepr(schema.integer(42),           'schema.integer(42)')
        self.assertRepr(schema.integer.min(0),        'schema.integer.min(0)')
        self.assertRepr(schema.integer.max(1),        'schema.integer.max(1)')
        self.assertRepr(schema.integer.between(0, 1), 'schema.integer.between(0, 1)')
        self.assertRepr(schema.integer.positive,      'schema.integer.positive')
        self.assertRepr(schema.integer.non_positive,  'schema.integer.non_positive')
        self.assertRepr(schema.integer.negative,      'schema.integer.negative')
        self.assertRepr(schema.integer.non_negative,  'schema.integer.non_negative')
        self.assertRepr(schema.integer.zero,          'schema.integer.zero')
        self.assertRepr(schema.integer.multiple(5),   'schema.integer.multiple(5)')

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.integer.nullable, 'schema.integer.nullable')

    def test_float_type_representation(self):
        self.assertRepr(schema.float,                   'schema.float')
        self.assertRepr(schema.float(3.14),             'schema.float(3.14)')
        self.assertRepr(schema.float.min(0.0),          'schema.float.min(0.0)')
        self.assertRepr(schema.float.max(1.0),          'schema.float.max(1.0)')
        self.assertRepr(schema.float.between(0.0, 1.0), 'schema.float.between(0.0, 1.0)')
        self.assertRepr(schema.float.precision(9),      'schema.float.precision(9)')
        self.assertRepr(schema.float.positive,          'schema.float.positive')
        self.assertRepr(schema.float.non_positive,      'schema.float.non_positive')
        self.assertRepr(schema.float.negative,          'schema.float.negative')
        self.assertRepr(schema.float.non_negative,      'schema.float.non_negative')
        self.assertRepr(schema.float.zero,              'schema.float.zero')

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.float.nullable, 'schema.float.nullable')

    def test_string_type_representation(self):
        self.assertRepr(schema.string,                      'schema.string')
        self.assertRepr(schema.string('banana'),            "schema.string('banana')")
        self.assertRepr(schema.string.length(32),           'schema.string.length(32)')
        self.assertRepr(schema.string.length(1, 64),        'schema.string.length(1, 64)')
        self.assertRepr(schema.string.min_length(1),        'schema.string.min_length(1)')
        self.assertRepr(schema.string.max_length(128),      'schema.string.max_length(128)')
        self.assertRepr(schema.string.empty,                'schema.string.empty')
        self.assertRepr(schema.string.non_empty,            'schema.string.non_empty')
        self.assertRepr(schema.string.pattern(r'[0-9\-_]'), "schema.string.pattern(r'[0-9\-_]')")
        self.assertRepr(schema.string.uri,                  'schema.string.uri')
        self.assertRepr(schema.string.alphabetic,           'schema.string.alphabetic')
        self.assertRepr(schema.string.numeric,              'schema.string.numeric')
        self.assertRepr(schema.string.numeric(1),           'schema.string.numeric(1)')
        self.assertRepr(schema.string.numeric(0, 1),        'schema.string.numeric(0, 1)')
        self.assertRepr(schema.string.alpha_num,            'schema.string.alpha_num')
        self.assertRepr(schema.string.lowercase,            'schema.string.lowercase')
        self.assertRepr(schema.string.uppercase,            'schema.string.uppercase')
        self.assertRepr(schema.string.contains('substr'),   "schema.string.contains('substr')")

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.string.nullable, 'schema.string.nullable')

    def test_timestamp_type_representation(self):
        self.assertRepr(schema.timestamp,     'schema.timestamp')
        self.assertRepr(schema.timestamp.iso, 'schema.timestamp.iso')

        self.assertRepr(schema.timestamp('21-10-2015 04:29 pm'),
                       "schema.timestamp('2015-10-21T16:29:00+00:00')")

        self.assertRepr(schema.timestamp('21-10-2015 04:29 pm').iso,
                       "schema.timestamp('2015-10-21T16:29:00+00:00').iso")

        self.assertRepr(schema.timestamp.min('01/01/2015'),
                       "schema.timestamp.min('2015-01-01T00:00:00+00:00')")
        
        self.assertRepr(schema.timestamp.max('01/01/2015'),
                       "schema.timestamp.max('2015-01-01T00:00:00+00:00')")

        self.assertRepr(
            schema.timestamp.between('01/01/2015', '21/10/2015'),
            "schema.timestamp.between('2015-01-01T00:00:00+00:00', '2015-10-21T00:00:00+00:00')"
        )

        self.assertRepr(schema.timestamp.format('%Y-%m-%d %H:%M:%S'),
                       "schema.timestamp.format('%Y-%m-%d %H:%M:%S')")

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.timestamp.nullable, 'schema.timestamp.nullable')


    def test_array_type_representation(self):
        self.assertRepr(schema.array,                'schema.array')
        self.assertRepr(schema.array([]),            'schema.array([])')
        self.assertRepr(schema.array.length(10),     'schema.array.length(10)')
        self.assertRepr(schema.array.length(1, 2),   'schema.array.length(1, 2)')
        self.assertRepr(schema.array.min_length(1),  'schema.array.min_length(1)')
        self.assertRepr(schema.array.max_length(10), 'schema.array.max_length(10)')
        self.assertRepr(schema.array.empty,          'schema.array.empty')
        self.assertRepr(schema.array.non_empty,      'schema.array.non_empty')

        self.assertRepr(schema.array.unique,
                       'schema.array.unique')
        self.assertRepr(schema.array.unique(lambda a, b: a != b),
                       'schema.array.unique(<predicate>)')

        self.assertRepr(schema.array([schema.integer(0), schema.integer(1)]),
                       'schema.array([schema.integer(0), schema.integer(1)])')

        self.assertRepr(schema.array.contains(schema.integer(42)),
                       'schema.array.contains(schema.integer(42))')
        self.assertRepr(schema.array.contains_one(schema.boolean),
                       'schema.array.contains_one(schema.boolean)')
        self.assertRepr(schema.array.contains_many(schema.string('banana')),
                       "schema.array.contains_many(schema.string('banana'))")
        self.assertRepr(schema.array.contains_all([schema.string('banana'), schema.string('')]),
                       "schema.array.contains_all([schema.string('banana'), schema.string('')])")

        self.assertRepr(
            schema.array.contains(schema.object({
                'id': schema.integer(1)
            })),
            "schema.array.contains(schema.object({" + "\n" +
            "    'id': schema.integer(1)" + "\n" +
            "}))"
        )

        self.assertRepr(
            schema.array([
                schema.integer(1),
                schema.integer(2),
                schema.integer(3)
            ]),
            "schema.array([" + "\n" +
            "    schema.integer(1)," + "\n" +
            "    schema.integer(2)," + "\n" +
            "    schema.integer(3)" + "\n" +
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
            "    schema.integer(1)," + "\n" +
            "    schema.integer(2)," + "\n" +
            "    schema.object({" + "\n" +
            "        'id': schema.string.numeric" + "\n" +
            "    })" + "\n" +
            "])"
        )

        self.assertRepr(
            schema.object({
                'items': schema.array([schema.object({
                    'id': schema.string.numeric
                })])
            }),
            "schema.object({" + "\n" +
            "    'items': schema.array([schema.object({" + "\n" +
            "        'id': schema.string.numeric" + "\n" +
            "    })])" + "\n" +
            "})"
        )

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.array.nullable, 'schema.array.nullable')

    def test_array_of_type_representation(self):
        self.assertRepr(schema.array.of(schema.integer),
                       'schema.array_of(schema.integer)')

        self.assertRepr(schema.array.of(schema.integer).empty,
                       'schema.array_of(schema.integer).empty')

        self.assertRepr(schema.array.of(schema.integer).non_empty,
                       'schema.array_of(schema.integer).non_empty')

        self.assertRepr(schema.array.of(schema.integer).length(2),
                       'schema.array_of(schema.integer).length(2)')

        self.assertRepr(schema.array.of(schema.integer).length(1, 10),
                       'schema.array_of(schema.integer).length(1, 10)')

        self.assertRepr(schema.array.of(schema.integer).min_length(1),
                       'schema.array_of(schema.integer).min_length(1)')

        self.assertRepr(schema.array.of(schema.integer).max_length(10),
                       'schema.array_of(schema.integer).max_length(10)')

        self.assertRepr(schema.array.of(schema.string).unique,
                       'schema.array_of(schema.string).unique')

        self.assertRepr(schema.array.of(schema.string).unique(lambda a, b: a != b),
                       'schema.array_of(schema.string).unique(<predicate>)')

        self.assertRepr(
            schema.array.of(schema.object({
                'id': schema.string.numeric
            })),
            "schema.array_of(schema.object({" + "\n" +
            "    'id': schema.string.numeric" + "\n" +
            "}))"
        )

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.array_of(schema.integer),
                           'schema.array_of(schema.integer)')
            self.assertRepr(schema.array.of(schema.integer).nullable,
                           'schema.array_of(schema.integer).nullable')

    def test_object_type_representation(self):
        self.assertRepr(schema.object,               'schema.object')
        self.assertRepr(schema.object({}),           'schema.object({})')
        self.assertRepr(schema.object.length(1),     'schema.object.length(1)')
        self.assertRepr(schema.object.length(0, 1),  'schema.object.length(0, 1)')
        self.assertRepr(schema.object.min_length(1), 'schema.object.min_length(1)')
        self.assertRepr(schema.object.max_length(1), 'schema.object.max_length(1)')
        self.assertRepr(schema.object.empty,         'schema.object.empty')
        self.assertRepr(schema.object.non_empty,     'schema.object.non_empty')
        
        self.assertRepr(
            schema.object({
                'id': schema.integer.positive
            }),
            "schema.object({" + "\n" +
            "    'id': schema.integer.positive" + "\n" +
            "})"
        )

        self.assertRepr(
            schema.object({
                'id': schema.integer.positive
            }).strict,
            "schema.object({" + "\n" +
            "    'id': schema.integer.positive" + "\n" +
            "}).strict"
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
            "    'attrs': schema.object({" + "\n" +
            "        'height': schema.float," + "\n" +
            "        'width': schema.float" + "\n" +
            "    })," + "\n" +
            "    'id': schema.integer.positive" + "\n" +
            "})"
        )

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.object.nullable, 'schema.object.nullable')

    def test_object_type_with_renamed_keys_representation(self):
        self.assertRepr(schema.object @ {},                  'schema.object')
        self.assertRepr(schema.object.empty @ {},             'schema.object.empty')
        self.assertRepr(schema.object.empty @ {'key': 'val'}, 'schema.object.empty')

        self.assertRepr(
            schema.object({
                'id': schema.string,
                'project_id': schema.integer,
                'user': schema.object({
                    'user_id': schema.string.numeric,
                    'name': schema.string.non_empty
                }).strict
            }) @ {
                'project_id': 'region_id',
                'user.user_id': 'id',
                'key': 'new_key'
            },
            '\n'.join([
                "schema.object({",
                "    'id': schema.string,",
                "    'region_id': schema.integer,",
                "    'user': schema.object({",
                "        'id': schema.string.numeric,",
                "        'name': schema.string.non_empty",
                "    }).strict",
                "})"
            ])
        )

    def test_any_type_representation(self):
        self.assertRepr(schema.any, 'schema.any')

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.any.nullable, 'schema.any.nullable')

    def test_any_of_type_representation(self):
        self.assertRepr(schema.any_of(schema.integer, schema.string.numeric, schema.null),
                       'schema.any_of(schema.integer, schema.string.numeric, schema.null)')

        self.assertRepr(schema.any_of(schema.integer(0), schema.integer(1)),
                       'schema.any_of(schema.integer(0), schema.integer(1))')

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.any_of(schema.integer, schema.string.numeric).nullable,
                           'schema.any_of(schema.integer, schema.string.numeric).nullable')

    def test_one_of_type_representation(self):
        self.assertRepr(schema.one_of(schema.integer, schema.string.numeric, schema.null),
                       'schema.one_of(schema.integer, schema.string.numeric, schema.null)')

        self.assertRepr(schema.one_of(schema.integer(0), schema.integer(1)),
                       'schema.one_of(schema.integer(0), schema.integer(1))')

        self.assertRepr(schema.boolean(True) | schema.null,
                       'schema.one_of(schema.boolean(True), schema.null)')

        self.assertRepr(schema.boolean(False) | schema.string('false') | schema.null,
                       "schema.one_of(schema.boolean(False), schema.string('false'), schema.null)")

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.one_of(schema.integer, schema.string.numeric).nullable,
                           'schema.one_of(schema.integer, schema.string.numeric).nullable')

    def test_enum_type_representation(self):
        self.assertRepr(schema.enum(1, 2, 3),       'schema.enum(1, 2, 3)')
        self.assertRepr(schema.enum('a', 'b', 'c'), "schema.enum('a', 'b', 'c')")
        self.assertRepr(schema.enum(0, 1, None),    'schema.enum(0, 1, None)')

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertRepr(schema.enum(0, 1).nullable,
                           'schema.enum(0, 1).nullable')

    def test_undefined_type_representation(self):
        self.assertRepr(schema.undefined, 'schema.undefined')
