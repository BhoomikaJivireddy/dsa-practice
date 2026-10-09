"""LeetCode 242: Valid Anagram
Approach: two strings are anagrams if their sorted characters match.
Time: O(n log n)  Space: O(n)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
