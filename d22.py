# You are given an array temperatures.

# For every day, find how many days you have to wait until a warmer temperature.

# If there is no warmer day, return 0.

# Example
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

# Answer:

# [1, 1, 4, 2, 1, 1, 0, 0]

def dailyTemperatures(temperatures):

    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):

        while stack and temperatures[i] > temperatures[stack[-1]]:

            previous = stack.pop()

            answer[previous] = i - previous

        stack.append(i)

    return answer
temp=[73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temp))