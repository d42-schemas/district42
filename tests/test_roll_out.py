import unittest
from copy import deepcopy

from district42.helpers import roll_out


class TestRollOut(unittest.TestCase):

    def test_roll_out_empty_dict(self):
        self.assertDictEqual(roll_out({}), {})

    def test_roll_out_simple_keys(self):
        keys = {
            'none_key': None,
            'bool_key': True,
            'int_key': 42,
            'float_key': 3.14,
            'str_key': 'banana',
            'list_key': [],
            'dict_key': {},
        }
        self.assertDictEqual(roll_out(deepcopy(keys)), keys)

    def test_roll_out_composite_keys(self):
        keys = {
            'key1': 'val-1',
            'key2.key3': 'val-2-3',
            'key4.key5': 'val-4-5',
            'key6.key7.key8': 'val-6-7-8',
        }
        expected = {
            'key1': 'val-1',
            'key2': {
                'key3': 'val-2-3',
            },
            'key4': {
                'key5': 'val-4-5',
            },
            'key6': {
                'key7': {
                    'key8': 'val-6-7-8',
                }
            }
        }
        self.assertDictEqual(roll_out(keys), expected)

    def test_roll_out_sibling_composite_keys(self):
        keys = {
            'key1.key2': 'val-1-2',
            'key1.key3.key4': 'val-1-3-4',
            'key1.key3.key5': 'val-1-3-5',
        }
        expected = {
            'key1': {
                'key2': 'val-1-2',
                'key3': {
                    'key4': 'val-1-3-4',
                    'key5': 'val-1-3-5',
                },
            },
        }
        self.assertDictEqual(roll_out(keys), expected)

    def test_roll_out_nested_composite_keys(self):
        keys = {
            'key1': {
                'key2.key3': 'val-1-2-3',
            },
            'key4.key5': {
                'key6.key7': 'val-4-5-6-7',
                'key8.key9': 'val-4-5-8-9',
                'key10': 'val-4-5-10',
                'key11': {},
            },
            'key12.key13': {},
            'key14': {},
        }
        expected = {
          'key1': {
            'key2': {
              'key3': 'val-1-2-3',
            }
          },
          'key4': {
            'key5': {
              'key6': {
                'key7': 'val-4-5-6-7',
              },
              'key8': {
                'key9': 'val-4-5-8-9',
              },
              'key10': 'val-4-5-10',
              'key11': {},
            }
          },
          'key12': {
            'key13': {},
          },
          'key14': {},
        }
        self.assertDictEqual(roll_out(keys), expected)

    def test_roll_out_dotted_keys(self):
        keys = {
            'key1.key2': 'val-1-2',
            'key3\.key4': 'val-3-4',
        }
        expected = {
            'key1': {
                'key2': 'val-1-2',
            },
            'key3\.key4': 'val-3-4',
        }
        self.assertDictEqual(roll_out(keys), expected)

    def test_roll_out_empty_keys(self):
        keys = {'': 'val1'}
        self.assertDictEqual(deepcopy(keys), roll_out(keys))

    def test_roll_out_non_string_keys(self):
        keys = {
            None: 'val1',
            1: 'val2',
        }
        self.assertDictEqual(deepcopy(keys), roll_out(keys))

    def test_it_copies_dict(self):
        keys = {
            'key1': 'val-1',
            'key2.key3': 'val-2-3',
        }
        copy = deepcopy(keys)
        roll_out(copy)
        self.assertDictEqual(copy, keys)
