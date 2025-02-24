# Leetcode link - https://leetcode.com/problems/min-stack/

# Using Two stacks - one actually & one to track min
# T: O(1) for all operations, S: O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Using Two stacks (Optimal - only push (elem, freq) into min stack)
# T: O(1) for all operations, S: O(n)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if val < self.min_stack[-1][0]:
                self.min_stack.append((val, 1))
            else:
                # greater than or equal to case
                elem, elem_freq = self.min_stack[-1]
                self.min_stack.pop()
                self.min_stack.append((elem, elem_freq+1))
        else:
            self.min_stack.append((val, 1))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            elem, elem_freq = self.min_stack[-1]
            if elem_freq == 1:
                self.min_stack.pop()
            else:
                self.min_stack.pop()
                self.min_stack.append((elem, elem_freq-1))
        
    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        return self.min_stack[-1][0] if self.min_stack else -1

