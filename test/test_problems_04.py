import pytest
from easy_02 import Solution as SolutionEasy2
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []


@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3], -5, [1, 2]),
    ([0, 4, -4], 0, [1, 2]),
    ([1, 2, 3, 4, 5], 9, [3, 4]),
    ([1, 1], 2, [0, 1]),
    ([10, 15, 3, 7], 17, [0, 3]),
])
def test_two_sum(nums, target, expected):
    solution = Solution()
    result = solution.twoSum(nums, target)
    # Check that the result indices are in the expected order or reversed
    assert sorted(result) == sorted(expected), f"Expected indices {expected} but got {result}"
    # Verify the sum of the elements at the indices equals the target
    assert nums[result[0]] + nums[result[1]] == target, "Sum does not match target"
    # Ensure indices are distinct
    assert result[0] != result[1], "Indices must be distinct"