class Solution(object):
    def containsDuplicate(self, nums):
        return False if len(set(nums)) == len(nums) else True

        # if len(set(nums)) == len(nums):
        #     return False
        # return True


s = Solution()
print(s.containsDuplicate([1, 1, 2, 3]))
