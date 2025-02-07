# Leetcode link - https://leetcode.com/problems/valid-anagram/
from typing import *

class Solution:
    # Sorting -> T: O(nlogn + mlogm), S: O(1) / O(n+m) based on sorting
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)
    
    # HashTable -> T: O(n+m), S: O(1) since we have at most 26 different characters.
    def isAnagram_hashtable(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
    
    # HashTable Optimal (using single direct array) -> T: O(n+m), S: O(1) since we have at most 26 different characters.
    def isAnagram_hashtable(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1 # increment
            count[ord(t[i])-ord('a')] -= 1 # decrement

        for val in count:
            if val != 0:
                return False
        return True