from baby_steps import given, then, when
from pytest import raises

from district42 import make_required, schema
from district42.errors import DeclarationError
from district42.types import DictSchema, optional


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
        assert sch.props.keys == {key: (val, False) for key, val in keys.items()}


def test_dict_optional_keys_declaration():
    with given:
        keys = {
            "id": schema.int(42),
            "name": schema.str("banana"),
            optional("created_at"): schema.int,
        }
        props = {
            "id": (schema.int(42), False),
            "name": (schema.str("banana"), False),
            "created_at": (schema.int, True),
        }

    with when:
        sch = schema.dict(keys)

    with then:
        assert sch.props.keys == props


def test_dict_optional_keys_all_made_required_declaration():
    with given:
        keys = {
            "id": schema.int(42),
            optional("name"): schema.str("banana"),
            optional("created_at"): schema.int,
        }
        props = {
            "id": (schema.int(42), False),
            "name": (schema.str("banana"), False),
            "created_at": (schema.int, False),
        }

    with when:
        sch = make_required(schema.dict(keys))

    with then:
        assert sch.props.keys == props


def test_dict_optional_keys_one_made_required_declaration():
    with given:
        keys = {
            "id": schema.int(42),
            optional("name"): schema.str("banana"),
            optional("created_at"): schema.int,
        }
        props = {
            "id": (schema.int(42), False),
            "name": (schema.str("banana"), False),
            "created_at": (schema.int, True),
        }

    with when:
        sch = make_required(schema.dict(keys), {"name"})

    with then:
        assert sch.props.keys == props


def test_dict_make_required_invalid_schema_type_declaration_error():
    with given:
        sch = schema.list([schema.str("banana")])

    with when, raises(Exception) as exception:
        make_required(sch)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == f"Inappropriate type of schema {sch!r} ({type(sch)!r})"


def test_dict_make_required_invalid_keys_type_declaration_error():
    with given:
        keys = {
            "id": schema.int(42),
            optional("name"): schema.str("banana"),
            optional("created_at"): schema.int,
        }
        keys_req = "name"

    with when, raises(Exception) as exception:
        make_required(schema.dict(keys), keys_req)

    with then:
        assert exception.type is DeclarationError
        assert str(
            exception.value) == f"Inappropriate type of keys {keys_req!r} ({type(keys_req)!r})"


def test_dict_make_required_nonexisting_keys_declaration_error():
    with given:
        keys = {
            "id": schema.int(42),
            optional("name"): schema.str("banana"),
            optional("created_at"): schema.int,
        }
        keys_req = {"banana"}

    with when, raises(Exception) as exception:
        make_required(schema.dict(keys), keys_req)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == f"Nonexisting key {list(keys_req)[0]!r}"


def test_dict_make_required_empty_dict_declaration_error():
    with given:
        keys = {}

    with when, raises(Exception) as exception:
        make_required(schema.dict(keys))

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "DictSchema must not be empty"


def test_dict_make_required_relaxed_dict_declaration_error():
    with given:
        keys = {
            "id": schema.int(42),
            optional("name"): schema.str("banana"),
            optional("created_at"): schema.int,
            ...: ...
        }

    with when, raises(Exception) as exception:
        make_required(schema.dict(keys))

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "DictSchema must not be relaxed"


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
