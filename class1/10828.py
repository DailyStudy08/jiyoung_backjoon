import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    query = input().strip()
    if query == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif query == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif query == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif query == 'size':
        print(len(stack))
    else:
        query = query.split()
        stack.append(int(query[1]))