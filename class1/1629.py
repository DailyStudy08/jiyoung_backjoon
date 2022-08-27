import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())

tmp = a
lst = []
while b != 0:
    lst.append(b%2)
    b //= 2

dp = [0]*len(lst)
dp[0] = tmp%c
for i in range(1,len(lst)):
    dp[i] = (tmp%c)*(tmp%c)%c
    tmp = dp[i]

ans = 1

for i in range(len(lst)):
    if lst[i]:
        ans *= (lst[i]*dp[i])%c

print(ans%c)