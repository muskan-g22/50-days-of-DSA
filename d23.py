# You are given an expression in Reverse Polish Notation.

# Evaluate the expression and return the result.

# The possible operators are:

# +   -   *   /
# Example
# tokens = ["2", "1", "+", "3", "*"]

# Normal mathematical expression:

# (2 + 1) × 3

# Answer:

# 9

def evalRPN(tokens):

    stack = []

    for token in tokens:

        if token not in "+-*/":
            stack.append(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            else:
                result = int(a / b)

            stack.append(result)

    return stack[-1]


# Driver Code

tokens = input("Enter tokens separated by space: ").split()

answer = evalRPN(tokens)

print("Result:", answer)