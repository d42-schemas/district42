from typing import Any

import pytest
from baby_steps import given, then, when

from district42 import represent, schema


def test_const_representation():
    with given:
        sch = schema.const

    with when:
        res = represent(sch)

    with then:
        assert res == "schema.const"


@pytest.mark.parametrize(
    ("value", "expected_repr"),
    [
        (None, "schema.const(None)"),
        (True, "schema.const(True)"),
        (42, "schema.const(42)"),
        (3.14, "schema.const(3.14)"),
        ("banana", "schema.const('banana')")
    ]
)
def test_const_value_representation(value: Any, expected_repr: str):
    with given:
        sch = schema.const(value)

    with when:
        res = represent(sch)

    with then:
        assert res == expected_repr
