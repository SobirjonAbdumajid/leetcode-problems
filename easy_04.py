# # 1
# class Solution(object):
#     def findClosestNumber(self, nums):
#         evens = list(map(abs, nums))
#
#         closest = min(evens)
#         if closest in nums:
#             return closest
#         return closest * -1


# # 2
# class Solution(object):
#     def findClosestNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return min(nums, key=lambda x: (abs(x), -x))


# 3
# class Solution:
#     def findClosestNumber(self, nums):
#         min_value = nums[0]
#         for num in nums:
#             if abs(num) < abs(min_value) or (abs(num) == abs(min_value) and num > min_value):
#                 min_value = num
#         return min_value


# 4
class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest):
                closest = x

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        return closest


solution = Solution()
result = solution.findClosestNumber([2, -1, 1, 1, -5, 4, -1, 100000])
print(result)


