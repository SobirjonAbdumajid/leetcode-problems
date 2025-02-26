import pytest
from for_students import even_index_chars, get_second_largest


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("aoapalakajahag", "aaaaaaa"),
        ("hello", "hlo"),
        ("abc", "ac"),
        (4, TypeError),
    ]
)
def test_even_index_chars_fail(input_text, expected_output):
    if expected_output == TypeError:
        with pytest.raises(expected_output):
            assert even_index_chars(input_text) == expected_output

    result = even_index_chars(input_text)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_numbers, expected_output",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8),
        ([10, 11, 12], 11),
        ([5, 5, 5, 4], 4),
    ]
)
def test_get_second_largest_fail(input_numbers, expected_output):
    result = get_second_largest(input_numbers)
    assert result == expected_output
