from baby_steps import given, then, when
from pytest import raises

from district42 import schema
from district42.errors import DeclarationError
from district42.types import DictSchema


def test_dict_declaration():
    with when:
        sch = schema.dict

    with then:
        assert isinstance(sch, DictSchema)


def test_dict_empty_keys_declaration():
    with given:
        keys = {}

    with when:
        sch = schema.dict(keys)

    with then:
        assert sch.props.keys == keys


def test_dict_invalid_type_declaration_error():
    with when, raises(Exception) as exception:
        schema.dict([])

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == ("`schema.dict` value must be an instance of 'dict', "
                                        "instance of 'list' [] given")


def test_dict_keys_declaration():
    with given:
        keys = {
            "id": schema.int(42),
            "name": schema.str("banana")
        }

    with when:
        sch = schema.dict(keys)

    with then:
        assert sch.props.keys == keys


def test_dict_already_declared_declaration_error():
    with given:
        keys = {}

    with when, raises(Exception) as exception:
        schema.dict(keys)(keys)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.dict({})` is already declared"


def test_dict_invalid_value_type_declaration_error():
    with when, raises(Exception) as exception:
        schema.dict({"key": {}})

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == ("`schema.dict` value must be an instance of 'Schema', "
                                        "instance of 'dict' {} given")
