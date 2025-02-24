# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         _dict = {}
#         for i, value in enumerate(nums):
#             # try:
#             _dict[value + nums[i]] = [nums.index(value), i]
#             # except:
#         print(_dict)
#         return _dict[target]


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         _dict = {}
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 print(nums[j])
#
#                 # try:
#                 _dict[nums[i] + nums[j]] = [i, j]
#                 # except:
#             # print(_dict)
#             return _dict[target]


# class Solution(object):
#     def twoSum(self, nums, target):
#         _dict = {}
#         for i, value in enumerate(nums, start=1):
#             try:
#                 _dict[value + nums[i]] = [nums.index(value), i]
#                 print(nums[i])
#             except:
#                 return _dict[target]


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         _dict = {}
#         _set = set()
#         for i in nums:
#             for j in nums:
#                 _dict[i + j] = [nums.index(j), nums.index(i)]
#                 _set.add(i + j)
#                 print(i)
#         print(_set)
#         return _dict[target]


# class Solution(object):
#     def twoSum(self, nums, target):
#         _set = set()
#         for num in nums:
#             if num in _set:
#                 return [index for index, value in enumerate(nums) if target - value in nums]
#             _set.add(target - num)


# class Solution(object):
#     def twoSum(self, nums, target):
#         for i, num in enumerate(nums):
#             if target - num in nums:
#                 # list_to_return = [i]
#                 # nums.insert(i, target)
#                 # list_to_return.append(i)
#                 return [i, nums.index(target - num)]


class Solution(object):
    def twoSum(self, nums, target):
        _dict = {}
        for index, num in enumerate(nums):
            value = target - num
            if value in _dict:
                return [_dict[value], index]
            _dict[num] = index


solution = Solution()
print(solution.twoSum([3, 3], 6))
print(solution.twoSum([3, 2, 3], 6))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([1, 2, 3, 4, 5], 9))
