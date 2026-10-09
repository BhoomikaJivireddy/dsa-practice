"""LeetCode 217: Contains Duplicate
Time: O(n)  Space: O(n)
"""
from typing import List


class Solution:
    # Approach 1: frequency dictionary
    def containsDuplicate(self, nums: List[int]) -> bool:
        fr = {}
        for i in nums:
            fr[i] = fr.get(i, 0) + 1
            if fr[i] > 1:
                return True
        return False

    # Approach 2: using set
    def containsDuplicateSet(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
