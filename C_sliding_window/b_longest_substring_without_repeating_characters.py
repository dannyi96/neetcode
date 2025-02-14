# Leetcode link - https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import *

class Solution:
    # Bruteforce. T: O(n*m), S: O(m),
    # - n is the length of the string and 
    # - m is the total number of unique characters in the string.
    def lengthOfLongestSubstring_bruteforce(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res