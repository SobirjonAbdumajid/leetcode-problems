import pytest
from easy_10 import Solution
print(1)


@pytest.mark.parametrize("s, t, expected", [
    # Valid anagrams
    ("anagram", "nagaram", True),
    ("listen", "silent", True),
    ("hello", "olleh", True),
    ("a", "a", True),
    # Invalid cases
    ("rat", "car", False),
    ("a", "b", False),
    ("abc", "ab", False),  # Different lengths
    ("aaab", "aabb", False),  # Same letters, different counts
    ("aabbc", "aabbd", False),  # Different characters
    ("abc", "def", False),  # No common characters
    # Edge cases
    ("", "", True),  # Empty strings (though constraints say length ≥ 1)
    ("😊😠", "😠😊", True),  # Unicode characters (follow-up scenario)
    # TypeError
    ("😊😠", 4.4, TypeError),  # Unicode characters (follow-up scenario)
])
def test_is_anagram(s, t, expected):
    solution = Solution()
    if expected is TypeError:
        with pytest.raises(TypeError):
            assert solution.isAnagram(s, t)
    else:
        assert solution.isAnagram(s, t) == expected
