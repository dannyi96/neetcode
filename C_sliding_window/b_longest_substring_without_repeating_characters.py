# Leetcode link - https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import *

class Solution:
    # Bruteforce. T: O(n*m), S: O(m)
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
    
    # Sliding window approach. T: O(n), S: O(m)
    def lengthOfLongestSubstring_sliding_window(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                # Remove left character, incr l by 1
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res
    
    # Sliding window approach. T: O(n), S: O(m)
    def lengthOfLongestSubstring_sliding_window_optimised(self, s: str) -> int:
        # Main idea - store index of duplicate char at r so we can directly set l
        charIndexMap = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] in charIndexMap:
                # directly set l to skip duplicate value occurance
                l = max(charIndexMap[s[r]] + 1, l)
            charIndexMap[s[r]] = r
            res = max(res, r-l+1)
        
        return res