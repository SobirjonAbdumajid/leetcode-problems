# # 1 - chala
# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         result = ""
#         index_i = ""
#         index_t = ""
#         for i in s:
#             if i in t:
#                 index_i += str(t.find(i))
#                 index_t += str(i.find(t))
#                 result += i
#         right_answer = "".join(sorted(index_i))
#         if result == s and right_answer == index_i:
#             return True
#         return False
        
# solution = Solution()
# result = solution.isSubsequence("", "lettt")
# print(result)

# 2

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pointer_s, pointer_t = 0, 0
        
        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
        
        return pointer_s == len(s)

solution = Solution()
result = solution.isSubsequence("", "lettt")
print(result)