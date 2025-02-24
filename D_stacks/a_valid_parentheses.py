# Leetcode link - https://leetcode.com/problems/valid-parentheses/

class Solution:
    # Brute force. T:O(n^2), S:O(n)
    def isValid_bruteforce(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''

    # Stack based. T:O(n), S:O(n)
    def isValid_stack(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False