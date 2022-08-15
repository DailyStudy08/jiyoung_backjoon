import sys
input = sys.stdin.read
n, *lst = map(int, input().split())
for i in sorted(lst):
    print(i)