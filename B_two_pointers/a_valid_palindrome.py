# Leetcode link - https://leetcode.com/problems/valid-palindrome/
from typing import *

class Solution:
    # Create needed string chars. 
    # Reverse & check. T: O(n), S: O(n)
    def isPalindrome_reverse_string(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum(): # Note - useful method isalnum
                newStr += c.lower()
        return newStr == newStr[::-1]
    
    # Two pointer based. T: O(n), S: O(1)
    def isPalindrome_two_pointers(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip all non alphanumeric characters from left side
            while l < r and not s[l].isalnum():
                l += 1
            # Skip all non alphanumeric characters from right side
            while r > l and not s[r].isalnum():
                r -= 1
            # check equality
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    # Making alphaNum check from scratch
    # def alphaNum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z') or 
    #             ord('a') <= ord(c) <= ord('z') or 
    #             ord('0') <= ord(c) <= ord('9'))