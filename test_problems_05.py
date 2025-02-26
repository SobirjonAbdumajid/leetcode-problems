import pytest
from for_students import even_index_chars, get_second_largest


@pytest.fixture(scope='function', autouse=True)
def test_problems():
    print("\nRunning test_problems")
    even_index_chars_data = ["aoapalakajahag"]
    get_second_largest_data = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34]
    ]
    yield {
        "get_second_largest": get_second_largest_data,
        "even_index_chars": even_index_chars_data,
        "get_second_largest_fail": [1, 2, 3, "4"]
    }
    print("\nFinished test_problems")


def test_get_second_largest(test_problems):
    data = test_problems["get_second_largest"]
    expected_results = [8, 15, 22, 28, 33]
    for i, nums in enumerate(data):
        result = get_second_largest(nums)
        assert result == expected_results[i]


def test_even_index_chars(test_problems):
    data = test_problems["even_index_chars"]
    expected_results = ["aaaaaaa"]
    for i, text in enumerate(data):
        result = even_index_chars(text)
        assert result == expected_results[i]


# def test_get_second_largest_fail(test_problems):
#     data = test_problems["get_second_largest_fail"]
#     assert get_second_largest(data) == TypeError
