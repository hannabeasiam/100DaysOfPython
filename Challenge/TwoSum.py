"""
    Leet Code 1. Two Sum
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """

    def two_sum(self):
        for i in range(len(self.nums) - 1):
            for x in range(i + 1, len(self.nums)):
                if self.target - self.nums[i] == self.nums[x]:
                  #  print(self.nums[i], self.nums[x])
                    return self.nums[i], self.nums[x]
            return False


result = Solution([2, 15, 11, 7], 9)
print(result.two_sum())
