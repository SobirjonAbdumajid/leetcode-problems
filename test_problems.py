from easy_04 import Solution as EasySolution4
from easy_05 import Solution as EasySolution5
import pytest


def test_closest_number():
    solution = EasySolution4()

    assert solution.findClosestNumber([2, 1, 1, -5, 4, -1, 100000]) == 1
    assert solution.findClosestNumber([-4, -2, 1, 8]) == 1
    assert solution.findClosestNumber([5, -5, 10, -10]) == 5
    assert solution.findClosestNumber([0, -1, 1, -2, 2]) == 0
    assert solution.findClosestNumber([-7, -5, -3, -1]) == -1



# 1
@pytest.mark.parametrize("nums, expected", [
    # Test positive closest
    ([2, 1, 3], 1),
    ([5, 3, 2], 2),
    # Test negative closest
    ([-1, -2, -3], -1),
    ([-4, 3, 5], 3),
    # Test tie (positive and negative), return positive
    ([1, -1], 1),
    ([-5, 5, 10], 5),
    # Test zero case
    ([0, 2, -2], 0),
    # Test mix of numbers
    ([-5, 2, 1, -1], 1),
    ([2, -1, 1, -5, 4, -1, 100000], 1),
    # Test all negatives
    ([-10, -3, -5], -3),
    # Test with zero and negatives
    ([0, -1, -2], 0),
])
def test_find_closest_number(nums, expected):
    solution = EasySolution4()
    assert solution.findClosestNumber(nums) == expected


# 2
def test_merge_alternately():
    solution = EasySolution5()

    assert solution.mergeAlternately("ab", "pqr") == "apbqr"
    assert solution.mergeAlternately("abc", "def") == "adbecf"
    assert solution.mergeAlternately("a", "xyz") == "axyz"
    assert solution.mergeAlternately("hello", "world") == "hweolrllod"
    assert solution.mergeAlternately("", "abc") == "abc"
    assert solution.mergeAlternately("abc", "") == "abc"
