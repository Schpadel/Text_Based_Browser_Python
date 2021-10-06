from collections import deque

n = int(input())
stack = deque()

for _ in range(0, n):
    action = input()
    if "PUSH" in action:
        stack.append(action.split(" ", 1)[1])
    if "POP" in action:
        stack.pop()

for _ in range(0, len(stack)):
    print(stack.pop())
