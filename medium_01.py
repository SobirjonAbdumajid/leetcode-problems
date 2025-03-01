class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        _dict = {}
        for i, value in enumerate(numbers):
            result = target - value
            if result in _dict:
                return [_dict[result], i+1]
            _dict[value] = i

numbers = [0,0,3,4]
target = 7
s = Solution()
print(s.twoSum(numbers, target))
