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

    # Backtracking based - backtrack immediately once invalid encountered
    # T: O(4^n / sqrt(n)) [number of valid sequences(Catalan number)]
    # S: O(n) (Recursion space) + O(4^n / sqrt(n)) ( storing output)
    '''
        Understanding the time & space complexity
        The number of valid sequences follows the Catalan number, which counts the number of valid ways to arrange balanced parentheses:
            Catalan(n) = (2n C n) / (n+1) = (2n)!/(n+1)!n!
        Using Stirling's approximation for factorial growth:
            Catalan(n) ~ 4^n / ( n^(3/2) * pi^(1/2) )
 
        Thus, the number of recursive calls, 
            which is proportional to Catalan(n) is upper-bounded by -> O(4^n / sqrt(n))
    '''
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
    
    # DP based.
    # T: O(4^n / sqrt(n)) [number of valid sequences(Catalan number)]
    # S: O(4^n / sqrt(n)) ( storing output) ( no recursion space )
    def generateParenthesis_dp(self, n: int) -> List[str]:
        res = [[] for _ in range(n+1)]  # DP table, where res[k] stores valid sequences for k pairs
        res[0] = [""]  # Base case: One way to have 0 pairs (empty string)

        for k in range(n + 1):  # Compute results for k pairs
            for i in range(k):  # i is the number of pairs inside the first '(' and ')'
                for left in res[i]:  # Get valid sequences for i pairs
                    for right in res[k-i-1]:  # Get valid sequences for remaining k-i-1 pairs
                        res[k].append("(" + left + ")" + right)  # Form a valid sequence
        
        return res[-1]  # Return results for n pairs