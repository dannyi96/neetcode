# Leetcode Link - https://leetcode.com/problems/generate-parentheses/
from typing import *

class Solution:
    # Bruteforce. T: O(2^(2n) * n), S: O(2^(2n) * n)
    def generateParenthesis_bruteforce(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False # unbalanced scenario
            return not open

        # Brute force - Trying all possibilities
        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs("")
        return res

    # Backtracking based. TODO
    def generateParenthesis_backtrack(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
    
    # DP based. TODO