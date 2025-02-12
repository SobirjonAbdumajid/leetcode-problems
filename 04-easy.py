# # 1
# class Solution(object):
#     def findClosestNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         evens = list(map(abs, nums))
#         print(evens)
#
#         closest = min(evens)
#         closest_negative = closest * -1
#         if closest in nums:
#             return closest
#         if closest_negative in nums:
#             return closest_negative



# class Solution(object):
#     def findClosestNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return min(nums, key=lambda x: (abs(x), -x))



class Solution:
    def findClosestNumber(self, nums):
        closest = nums[0]  # Dastlabki elementni eng yaqin deb belgilaymiz
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num  # 0 ga yaqin yoki teng bo‘lsa kattasini tanlaymiz
        return closest

solution = Solution()
result = solution.findClosestNumber([-4,-2,4,8])
print(result)


# print(abs(-2))


