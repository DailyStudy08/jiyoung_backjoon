import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
stack = deque()
for i in range(n):
    query = input().strip()
    if query == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif query == 'back':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif query == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif query == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif query == 'size':
        print(len(stack))
    elif query == 'pop_front':
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif query == 'pop_back':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        query = query.split()
        if query[0] == 'push_front':
            stack.appendleft(int(query[1]))
        elif query[0] == 'push_back':
            stack.append(int(query[1]))