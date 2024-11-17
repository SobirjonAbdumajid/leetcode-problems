class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        result = ""
        index = ""
        for i in s:
            if i in t:
                index += str(t.find(i))
                if int(index[-1]) < t.find(i):
                    return False
                print(int(index[-1]))
                # print(index)
                result += i
                # print(result)
        
        # for j, value in enumerate(index):
        #     try:
        #         print(int(index[j + 1]) > int(value))
        #     except:
        #         print('xato')
        print(index)
        if result == s:
            return True
        return False
        
solution = Solution()
result = solution.isSubsequence("word", "wbndoarp")
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