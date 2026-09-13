# Design a stack that supports:

# push(x)       → Add x
# pop()         → Remove top element
# top()         → Return top element
# getMin()      → Return minimum element

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(val, self.min_stack[-1])
            )

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return -1


# Driver Code

s = MinStack()

s.push(5)
s.push(3)
s.push(7)
s.push(2)

print("Top:", s.top())
print("Minimum:", s.getMin())

s.pop()

print("Top after pop:", s.top())
print("Minimum after pop:", s.getMin())