# # 1
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
        
#         word1 = [i for i in word1]
#         word2 = [i for i in word2]
        
#         counter = 0
#         for i in word1:
#             word2.insert(counter, i)            
#             counter += 2
#         return ''.join(word2)
        
# # 2
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         result = []
#         i, j = 0, 0
#
#         while i < len(word1) and j < len(word2):
#             result.append(word1[i])
#             result.append(word2[j])
#             i += 1
#             j += 1
#
#         result.extend(word1[i:])
#         result.extend(word2[j:])
#
#         return ''.join(result)


class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        len1 = len(word1)
        len2 = len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                result += word1[i]
            if i < len2:
                result += word2[i]
        return result

word1 = "ab"
word2 = "pqr"
solution = Solution()
result = solution.mergeAlternately(word1, word2)
print(result)