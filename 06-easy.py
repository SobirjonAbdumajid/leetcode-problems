class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        counter = 0
        for i in s:
            boolen = i in t
            if boolen:
                counter += 1
                if counter == len(s):
                    return True
        return False
        
solution = Solution()
result = solution.isSubsequence("", "awkmokmrkd")
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