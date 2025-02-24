class Solution(object):
    def maxNumberOfBalloons(self, text):
        _set = set()

        for i in "balon":
            _set.add(text.count(i) // "balloon".count(i))
        return min(_set)


s = Solution()
print(s.maxNumberOfBalloons("loonbalxballlpoon"))
