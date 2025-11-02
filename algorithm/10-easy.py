# # 1
# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
#
#         s_list = list(s)
#         for i in t[:]:
#             if i in s:
#                 try:
#                     s_list.remove(i)
#                 except ValueError:
#                     return False
#         if s_list == []:
#             return True
#         return False


# 2
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
