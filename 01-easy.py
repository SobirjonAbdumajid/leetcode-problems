class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the index of each number we encounter
        num_to_index = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            print(complement)
            
            # If complement exists in the dictionary, return the pair of indices
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Otherwise, store the current number with its index in the dictionary
            num_to_index[num] = i
            print(num_to_index)

# Example usage:
nums = [2, 1, 11, 15]
target = 25
solution = Solution()
print(solution.twoSum(nums, target)) # Output: [
