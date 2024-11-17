# # 1
# class Solution(object):
#     def findClosestNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         evens = list(map(abs, nums))
#         print(evens)
        
#         closest = min(evens)
#         closest_negative = closest * -1
#         if closest in nums:
#             return closest
#         if closest_negative in nums:
#             return closest_negative



class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums, key=lambda x: (abs(x), -x))


solution = Solution()
result = solution.findClosestNumber([-4,-2,1,4,8])
print(result)

