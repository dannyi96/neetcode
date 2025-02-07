# Leetcode link - https://leetcode.com/problems/group-anagrams/
from typing import *
from collections import defaultdict

class Solution:
    # Main idea is to use a hashmap
    # Choices for key ?
    #   - sorted chars of the string
    #   - tuple of count array

    # Using sorted chars in key -> T: O(m * nlogn), S: O(m*n) [ where n is max chars in a string, m is total strings ]
    def groupAnagrams_sorting(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)
        return list(res.values()) # res.values() -> <class 'dict_values'>, list(res.values()) -> <class 'list'>
    
    # Using tuple of count array -> T: O(m*n), S: O(m * 26) [ where n is max chars in a string, m is total strings ]
    def groupAnagrams_counter(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())