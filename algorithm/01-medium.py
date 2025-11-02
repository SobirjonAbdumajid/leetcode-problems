# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         nums.sort()
#         closest_sum = float('inf')
#
#         for i in range(len(nums) - 2):
#             left, right = i + 1, len(nums) - 1
#
#             while left < right:
#                 current_sum = nums[i] + nums[left] + nums[right]
#
#                 if abs(current_sum - target) < abs(closest_sum - target):
#                     closest_sum = current_sum
#
#                 if current_sum < target:
#                     left += 1
#                 elif current_sum > target:
#                     right -= 1
#                 else:
#                     return current_sum
#
#         return closest_sum
#
#
# #
# # class Solution(object):
# #     def findClosestNumber(self, nums):
# #         evens = list(map(abs, nums))
# #
# #         closest = min(evens)
# #         if closest in nums:
# #             return closest
# #         return closest * -1

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numbers = map(abs, nums)
        closest = min(numbers)
        return closest * -1




nums = [-1,20,1,-5]

solution = Solution()
result = solution.threeSumClosest(nums, 19)
print(result)
