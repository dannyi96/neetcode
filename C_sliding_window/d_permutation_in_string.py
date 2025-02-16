# Leetcode link - https://leetcode.com/problems/permutation-in-string/
# Check if a permutation of s1 exists as a substring of s2

from typing import *

class Solution:
    # Bruteforce. TODO
    def checkInclusion_bruteforce(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                # check for every substring of s2
                subStr = s2[i : j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False


