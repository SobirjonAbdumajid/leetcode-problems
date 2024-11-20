class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            print(complement)
            
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            num_to_index[num] = i
            print(num_to_index)

nums = [2, 1, 11, 15]
target = 25
solution = Solution()
print(solution.twoSum(nums, target))
