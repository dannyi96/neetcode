# Leetcode link - https://leetcode.com/problems/encode-and-decode-strings/
from typing import *

class Solution:
    # The main idea is to encode S1, S2, ..., Sn in the format <sizeofS1>#S1<sizeofS2>#S2....
    # Decoding is done in similar reverse manner
    # T: O(m) for encoding & decoding where m is sum of lengths of all the strings
    # S: O(1) for encoding & decoding (not including final string)
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # get size of word
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # get word
            i = j + 1
            j = i + length
            res.append(s[i:j])
            # update i
            i = j
        
        return res