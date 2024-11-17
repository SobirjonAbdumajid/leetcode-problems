class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        
        word1 = [i for i in word1]
        word2 = [i for i in word2]

        for value in word2:
            result.append(value)
            
        counter = 0
        for i in word1:
            result.insert(counter, i)
            counter += 2
        result = ''.join(result)
        return result
        

word1 = "ab"
word2 = "pqr"
solution = Solution()
result = solution.mergeAlternately(word1, word2)
print(result)