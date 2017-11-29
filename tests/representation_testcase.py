import unittest


class RepresentationTestCase(unittest.TestCase):

    def assertRepr(self, schema, representation):
        return self.assertEqual(repr(schema), representation)
