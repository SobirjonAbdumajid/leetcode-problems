# # class Solution(object):
# #     def isPalindrome(self, x):
# #         """
# #         :type x: int
# #         :rtype: bool
# #         """
# #         b = (x // 10) // 10
# #         o = x % 10
# #         if 0 < x < 10:
# #             return True
# #         if x < 100:
# #             b = x // 10
        
# #         if b == o:
# #             return True
# #         return False

        
class Solution(object):
    def isPalindrome(self, x):
        # Manfiy yoki 0 bilan tugaydigan (0 dan katta) sonlar palindrom bo‘lolmaydi
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Sonning teskarisini hosil qilish
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        print(reversed_half)

        
        # Agar son teng bo'lsa yoki uzunligi toq bo'lsa o‘rtasi teng chiqadi
        return x == reversed_half or x == reversed_half // 10

solution = Solution()
print(solution.isPalindrome(1904541))

# x = 10001

# reversed_half = 0
# while x > reversed_half:
#     reversed_half = reversed_half * 10 + x % 10
#     x //= 10
# print(reversed_half)

# print(x == reversed_half or x == reversed_half // 10)