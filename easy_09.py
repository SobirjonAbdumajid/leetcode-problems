# 1
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote_ = list(ransomNote)
        magazine_ = list(magazine)
        counter = 0
        for i in ransomNote_:
            if i in magazine_:
                magazine_.remove(i)
                counter += 1
        if counter == len(ransomNote_):
            return True
        return False


# # 2
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         d1 = {}
#         d2 = {}
#
#         A = sorted(list(set(ransomNote)))
#         B = sorted(list(set(magazine)))
#         for i in A:
#             if i not in B:
#                 return False
#         for i in ransomNote:
#             d1[i] = d1.get(i, 0) + 1
#         for i in magazine:
#             d2[i] = d2.get(i, 0) + 1
#         for i, j in d1.items():
#             if d1[i] > d2[i]:
#                 return False
#         return True


sol = Solution()
ransomNote = "aab"
magazine = "aasgb"
print(sol.canConstruct(ransomNote, magazine))
