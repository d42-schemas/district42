from baby_steps import given, then, when

from district42 import schema


def test_str_alphabet_and_len_declaration():
    with given:
        alphabet = "1234567890"
        min_length, max_length = 1, 32

    with when:
        sch = schema.str.alphabet(alphabet).len(min_length, max_length)

    with then:
        assert sch.props.alphabet == alphabet
        assert sch.props.min_len == min_length
        assert sch.props.max_len == max_length
