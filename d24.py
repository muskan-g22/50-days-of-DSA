# Design a queue using only stacks.

# The queue must support:

# push(x)   → Add x to the queue
# pop()     → Remove the front element
# peek()    → Return the front element
# empty()   → Check whether queue is empty

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        self.input_stack.append(x)

    def pop(self):
        self.peek()
        return self.output_stack.pop()

    def peek(self):
        if not self.output_stack:

            while self.input_stack:
                self.output_stack.append(
                    self.input_stack.pop()
                )

        return self.output_stack[-1]

    def empty(self):
        return not self.input_stack and not self.output_stack

q = MyQueue()

# Push elements
q.push(10)
q.push(20)
q.push(30)

print("Front element:", q.peek())

# Pop elements
print("Removed:", q.pop())
print("Removed:", q.pop())

# Add another element
q.push(40)

print("Front element:", q.peek())

print("Removed:", q.pop())
print("Is queue empty?", q.empty())