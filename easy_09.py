class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        print(set(ransomNote), len(set(ransomNote)), set(magazine), len(set()))
        if ransomNote == magazine or len(ransomNote) == len(magazine) and len(set(ransomNote)) == len(set(magazine)):
            return True
        return False


sol = Solution()
ransomNote = "aa"
magazine = "aab"
print(sol.canConstruct(ransomNote, magazine))
