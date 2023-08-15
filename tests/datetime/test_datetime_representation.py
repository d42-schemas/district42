from datetime import datetime

from baby_steps import given, then, when

from district42 import represent, schema


def test_datetime_representation():
    with given:
        sch = schema.datetime

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.datetime"


def test_datetime_value_representation():
    with given:
        dt = datetime.now()
        sch = schema.datetime(dt)

    with when:
        res = represent(sch)

    with then:
        assert res == f"schema.datetime({dt!r})"
