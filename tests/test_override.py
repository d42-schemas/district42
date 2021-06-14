from unittest.mock import Mock, call

from baby_steps import given, then, when
from pytest import raises

from district42 import Schema, schema


def test_non_implemented_invert():
    with when, raises(Exception) as exception:
        schema.str.__invert__()

    with then:
        assert exception.type is AttributeError


def test_non_implemented_mod():
    with when, raises(Exception) as exception:
        schema.str.__mod__(None)

    with then:
        assert exception.type is AttributeError


def test_override_invert():
    with given:
        mock_ = Mock()
        Schema.__override__("__invert__", mock_)

    with when:
        schema.str.__invert__()

    with then:
        assert mock_.mock_calls == [call()]


def test_override_mod():
    with given:
        mock_ = Mock()
        Schema.__override__("__mod__", mock_)

    with when:
        schema.str.__mod__()

    with then:
        assert mock_.mock_calls == [call()]
