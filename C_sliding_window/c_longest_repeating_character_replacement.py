# Leetcode link - https://leetcode.com/problems/longest-repeating-character-replacement/
from typing import *

class Solution:
    # Bruteforce. T: O(n^2), S: O(m) [ n is the length of the string and m is the total number of unique characters in the string]
    def characterReplacement_bruteforce(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            # Basic idea - for each character -> how far can we go with constraints ( k replacements )
            count = {}
            maxf = 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res
    
    # Sliding window optimised (more intuitive). T: O(n), S: O(m)
    def characterReplacement_sliding_window_optimised(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxF = 0
        
        l = 0
        for r in range(len(s)):
            # update counter & max frequent character
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, count[s[r]])
            
            # if windows exceeds constraint, update l accordingly
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res