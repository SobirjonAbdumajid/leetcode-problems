class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result = ""
        index_i = ""
        index_t = ""
        for i in s:
            if i in t:
                index_i += str(t.find(i))
                index_t += str(i.find(t))
                result += i
        right_answer = "".join(sorted(index_i))
        if result == s and right_answer == index_i:
            return True
        return False
        
solution = Solution()
result = solution.isSubsequence("", "lettt")
print(result)


# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        


# M = 1000
# CM = 900
# XC = 90
# IV = 4
# III = 3
# L = 50
# V = 5 
# III = 3

# print(III)