# put your python code here
import sys
from collections import deque

stack = deque()
text = input()

text.replace(" ", "")

for char in text:
    if char == "(":
        stack.append(char)
    if char == ")":
        if not stack:
            print("ERROR")
            sys.exit()
        stack.pop()

if stack:
    print("ERROR")
else:
    print("OK")
