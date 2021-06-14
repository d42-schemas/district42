from baby_steps import given, then, when

from district42 import represent, schema


def test_any_representation():
    with given:
        sch = schema.any

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.any"


def test_any_type_representation():
    with given:
        sch = schema.any(schema.none)

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.any(schema.none)"


def test_any_types_representation():
    with given:
        sch = schema.any(schema.int, schema.str)

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.any(schema.int, schema.str)"


def test_any_types_with_values_representation():
    with given:
        sch = schema.any(schema.int(42), schema.str("banana"))

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.any(schema.int(42), schema.str('banana'))"
