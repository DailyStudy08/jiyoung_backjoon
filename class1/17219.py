import sys
input = sys.stdin.readline


n, m = map(int, input().split())

dic = {}

for i in range(n):
    a,b =  input().split()
    dic[a] = b

for i in range(m):
    c = input().strip()
    print(dic[c])