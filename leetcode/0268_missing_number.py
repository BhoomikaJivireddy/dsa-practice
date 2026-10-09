"""LeetCode 268: Missing Number
Approach: expected sum n(n+1)/2 minus actual sum.
Time: O(n)  Space: O(1)
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        expected = (n * (n + 1)) // 2
        for i in range(0, n):
            total += nums[i]
        return expected - total
