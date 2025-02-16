class Solution(object):
    def containsDuplicate(self, nums):
        _set = set(nums)
        if len(_set) == len(nums):
            return False
        return True


s = Solution()
print(s.containsDuplicate([1, 2, 3]))
