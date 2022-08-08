import sys
input = sys.stdin.readline
output = sys.stdout.write
# f =  open('input.txt', 'r')
# input = f.readline

n = int(input())
lst = []

for i in range(n):
    s = input().split()
    if s[0] == 'push':
        lst.append(int(s[1]))
    elif s[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else :
            print(lst[0])
    elif s[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else :
            print(lst[-1])
    elif s[0] == 'size':
        print(len(lst))
    elif s[0] == 'empty':
        if len(lst):
            print(0)
        else :
            print(1)
    elif s[0] == 'pop':
        if len(lst) ==0 :
            print(-1)
        else :
            print(lst.pop(0))
