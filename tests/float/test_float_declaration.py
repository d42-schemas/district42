from baby_steps import given, then, when
from pytest import raises

from district42 import schema
from district42.errors import DeclarationError
from district42.types import FloatSchema


def test_float_declaration():
    with when:
        sch = schema.float

    with then:
        assert isinstance(sch, FloatSchema)


def test_float_value_declaration():
    with given:
        value = 3.14

    with when:
        sch = schema.float(value)

    with then:
        assert sch.props.value == value


def test_float_invalid_value_type_declaration_error():
    with when, raises(Exception) as exception:
        schema.float("3.14")

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == ("`schema.float` value must be an instance of 'float', "
                                        "instance of 'str' '3.14' given")


def test_float_already_declared_declaration_error():
    with when, raises(Exception) as exception:
        schema.float(3.14)(3.14)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.float(3.14)` is already declared"


def test_float_min_value_declaration():
    with given:
        min_value = 3.14

    with when:
        sch = schema.float.min(min_value)

    with then:
        assert sch.props.min == min_value


def test_float_invalid_min_value_type_declaration_error():
    with when, raises(Exception) as exception:
        schema.float.min("3.14")

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == ("`schema.float` value must be an instance of 'float', "
                                        "instance of 'str' '3.14' given")


def test_float_value_already_declared_min_declaration_error():
    with when, raises(Exception) as exception:
        schema.float.min(3.14)(3.2)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.float.min(3.14)` is already declared"


def test_float_min_value_already_declared_less_value_declaration_error():
    with given:
        sch = schema.float(3.14)

    with when, raises(Exception) as exception:
        sch.min(3.15)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == (
            f"`{sch!r}` min value must be less than or equal to 3.14, 3.15 given"
        )


def test_float_min_value_already_declared_min_declaration_error():
    with when, raises(Exception) as exception:
        schema.float.min(3.14).min(3.14)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.float.min(3.14)` is already declared"


def test_float_max_value_declaration():
    with given:
        max_value = 3.14

    with when:
        sch = schema.float.max(max_value)

    with then:
        assert sch.props.max == max_value


def test_float_invalid_max_value_type_declaration_error():
    with when, raises(Exception) as exception:
        schema.float.max("3.14")

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == ("`schema.float` value must be an instance of 'float', "
                                        "instance of 'str' '3.14' given")


def test_float_value_already_declared_max_declaration_error():
    with when, raises(Exception) as exception:
        schema.float.max(3.2)(3.14)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.float.max(3.2)` is already declared"


def test_float_max_value_already_declared_greater_value_declaration_error():
    with given:
        sch = schema.float(3.14)

    with when, raises(Exception) as exception:
        sch.max(3.13)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == (
            f"`{sch!r}` max value must be greater than or equal to 3.14, 3.13 given"
        )


def test_float_max_value_already_declared_max_declaration_error():
    with when, raises(Exception) as exception:
        schema.float.max(3.14).max(3.14)

    with then:
        assert exception.type is DeclarationError
        assert str(exception.value) == "`schema.float.max(3.14)` is already declared"


def test_float_min_max_value_declaration():
    with given:
        min_value, max_value = 3.14, 3.15

    with when:
        sch = schema.float.min(min_value).max(max_value)

    with then:
        assert sch.props.min == min_value
        assert sch.props.max == max_value


def test_float_min_max_with_value_declaration():
    with given:
        value = 3.14
        min_value, max_value = 3.13, 3.15

    with when:
        sch = schema.float(value).min(min_value).max(max_value)

    with then:
        assert sch.props.value == value
        assert sch.props.min == min_value
        assert sch.props.max == max_value
