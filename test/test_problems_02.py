# from easy_05 import Solution as SolutionEasy5
# from easy_08 import Solution as SolutionEasy8
# from easy_09 import Solution as SolutionEasy9
# import pytest
# from contextlib import nullcontext as does_not_raise
#
#
# class TestProblems:
#     @pytest.mark.parametrize("nums, expected", [
#         ([2, 1, 3], False),
#         ([2, 3, 3, 4, 5], True)
#     ])
#     def test_problem(self, nums: list[int], expected: bool):
#         solution = SolutionEasy8()
#         assert solution.containsDuplicate(nums) == expected
#
#
#     @pytest.mark.parametrize("word1, word2, expected, expectation", [
#         ("abc", "pqr", "apbqcr", does_not_raise()),
#         ("ab", ['pqrs'], "apbqrs", pytest.raises(AssertionError)),
#         ("abcd", "pq", "apbqcd", does_not_raise()),
#         ("a", "p", "ap", does_not_raise()),
#         ("", "xyz", "xyz", does_not_raise()),
#         ("xyz", "", "xyz", does_not_raise()),
#     ])
#     def test_merge_alternately(self, word1, word2, expected, expectation):
#         s = SolutionEasy5()
#         with expectation:
#             assert s.mergeAlternately(word1, word2) == expected
#
#         # if expected == TypeError:
#         #     with pytest.raises(TypeError):
#         #
#
#         # assert s.mergeAlternately(word1, word2) == expected
#
#
#     @pytest.mark.parametrize("ransom_note, magazine, expected", [
#         ("a", "b", False),
#         ("aa", "ab", False),
#         ("aa", "aab", True),
#         ("abc", "aabbcc", True),
#         ("abcd", "abc", False),
#         ("", "abc", True),
#         ("a", "", False),
#     ])
#     def test_can_construct(self, ransom_note, magazine, expected):
#         s = SolutionEasy9()
#         assert s.canConstruct(ransom_note, magazine) == expected
