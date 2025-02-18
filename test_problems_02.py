from easy_09 import Solution as SolutionEasy9
from easy_05 import Solution as SolutionEasy5
import pytest


@pytest.mark.parametrize("word1, word2, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
    ("a", "p", "ap"),
    ("", "xyz", "xyz"),
    ("xyz", "", "xyz"),
])
def test_merge_alternately(word1, word2, expected):
    s = SolutionEasy5()
    assert s.mergeAlternately(word1, word2) == expected


@pytest.mark.parametrize("ransom_note, magazine, expected", [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("abc", "aabbcc", True),
    ("abcd", "abc", False),
    ("", "abc", True),
    ("a", "", False),
])
def test_can_construct(ransom_note, magazine, expected):
    s = SolutionEasy9()
    assert s.canConstruct(ransom_note, magazine) == expected
