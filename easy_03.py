# # # class Solution(object):
# # #     def isPalindrome(self, x):
# # #         """
# # #         :type x: int
# # #         :rtype: bool
# # #         """
# # #         b = (x // 10) // 10
# # #         o = x % 10
# # #         if 0 < x < 10:
# # #             return True
# # #         if x < 100:
# # #             b = x // 10
#
# # #         if b == o:
# # #             return True
# # #         return False
#
#
# class Solution(object):
#     def isPalindrome(self, x):
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False
#
#         reversed_half = 0
#         while x > reversed_half:
#             reversed_half = reversed_half * 10 + x % 10
#             x //= 10
#         print(reversed_half)
#
#
#         return x == reversed_half or x == reversed_half // 10
#
# solution = Solution()
# print(solution.isPalindrome(1904541))
#
# # x = 10001
#
# # reversed_half = 0
# # while x > reversed_half:
# #     reversed_half = reversed_half * 10 + x % 10
# #     x //= 10
# # print(reversed_half)
#
# # print(x == reversed_half or x == reversed_half // 10)