from baby_steps import given, then, when

from district42 import represent, schema


def test_none_representation():
    with given:
        sch = schema.none

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.none"
