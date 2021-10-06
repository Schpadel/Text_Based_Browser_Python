from collections import deque

books = deque()

n = int(input())

for _ in range(0, n):
    action = input()

    if "BUY" in action:
        books.append(action.split(" ", 1)[1])
    if "READ" in action:
        print(books.pop())
