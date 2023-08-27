from uuid import uuid4

from baby_steps import given, then, when

from district42 import represent, schema


def test_uuid4_representation():
    with given:
        sch = schema.uuid4

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.uuid4"


def test_uuid4_value_representation():
    with given:
        value = uuid4()
        sch = schema.uuid4(value)

    with when:
        res = represent(sch)

    with then:
        assert res == f"schema.uuid4({value!r})"
