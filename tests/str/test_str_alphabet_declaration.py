import pytest
from baby_steps import given, then, when
from pytest import raises

from district42 import schema
from district42.errors import DeclarationError


def test_str_alphabet_declaration():
    with given:
        alphabet = "1234567890"

    with when:
        sch = schema.str.alphabet(alphabet)

    with then:
        assert sch.props.alphabet == alphabet


def test_str_invalid_alphabet_type_declaration_error():
    with when, raises(Exception) as exception:
        schema.str.alphabet(42)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == ("`schema.str` value must be an instance of 'str', "
                                        "instance of 'int' 42 given")


@pytest.mark.parametrize("alphabet", [
    "abn",
    "abnx",
])
def test_str_alphabet_with_value_declaration(alphabet: str):
    with when:
        sch = schema.str("banana").alphabet(alphabet)

    with then:
        assert sch.props.alphabet == alphabet


def test_str_alphabet_already_declared_value_declaration_error():
    with given:
        sch = schema.str("banana!")

    with when, raises(Exception) as exception:
        sch.alphabet("ab")

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == f"`{sch!r}` alphabet is missing letters: '!n'"


def test_str_alphabet_already_declared_alphabet_declaration_error():
    with when, raises(Exception) as exception:
        schema.str.alphabet("abn!").alphabet("abn!")

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.str.alphabet('abn!')` is already declared"


def test_str_value_already_declared_alphabet_declaration_error():
    with when, raises(Exception) as exception:
        schema.str.alphabet("abn!")("banana!")

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.str.alphabet('abn!')` is already declared"
