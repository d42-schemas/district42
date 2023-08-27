from baby_steps import given, then, when
from pytest import raises

from district42 import schema
from district42.errors import DeclarationError
from district42.types import ConstSchema


def test_const_declaration():
    with when:
        sch = schema.const

    with then:
        assert isinstance(sch, ConstSchema)


def test_const_value_declaration():
    with given:
        value = "banana"

    with when:
        sch = schema.const(value)

    with then:
        assert sch.props.value == value


def test_const_already_declared_declaration_error():
    with when, raises(Exception) as exception:
        schema.const(None)(None)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.const(None)` is already declared"
