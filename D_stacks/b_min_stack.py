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
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append((val, 1))
        else:
            self.min_stack[-1] = (self.min_stack[-1][0], self.min_stack[-1][1] + 1)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            if self.min_stack[-1][1] == 1:
                self.min_stack.pop()
            else:
                self.min_stack[-1] = (self.min_stack[-1][0], self.min_stack[-1][1] - 1)

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        return self.min_stack[-1][0] if self.min_stack else -1

# Optimal - Using one stack
# T: O(1) for all operations, S: O(n)
'''
The trick is to store modified values when pushing elements such that we can always retrieve the minimum efficiently.

Idea:
    Instead of storing just the element, 
        - we store a transformed value when pushing a new element that ensures we can retrieve the previous minimum when popping.

Implementation Details:
    - Maintain a single stack (stack) to store values.
    - Maintain a separate variable (minElement) to track the minimum element so far.
    - When pushing:
        - If the stack is empty, push diff(ie-0) and set minElement to that value.
        - If the new value is smaller than or equal to minElement, push a modified value to encode the previous minimum.
    - When popping:
        - If the popped value is less than minElement, it means it was a modified value, and we need to restore the previous minimum.
'''

class MinStack:
    def __init__(self):
        self.minElement = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0) # Diff
            self.minElement = x
        else:
            self.stack.append(x - self.minElement) # modified value which encodes the previous minimum
            if x < self.minElement:
                self.minElement = x

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            self.minElement = self.minElement - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.minElement
        else:
            return self.minElement

    def getMin(self) -> int:
        return self.minElement
