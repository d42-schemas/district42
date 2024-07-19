from datetime import date

from baby_steps import given, then, when

from district42 import represent, schema


def test_date_representation():
    with given:
        sch = schema.date

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.date"


def test_date_value_representation():
    with given:
        dt = date.today()
        sch = schema.date(dt)

    with when:
        res = represent(sch)

    with then:
        assert res == f"schema.date({dt!r})"
