"""LeetCode 1: Two Sum
Approach: one pass with a hash map of value -> index.
Time: O(n)  Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
