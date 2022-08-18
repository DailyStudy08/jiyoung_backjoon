import sys
# input = sys.stdin.read

n,r,c  = map(int, input().split())

x = []
y = []

for i in range(n-1, -1, -1):
    if c//(2**(i)):
        x.append(1)
    else:
        x.append(0)

    if r//(2**(i)):
        y.append(1)
    else:
        y.append(0)

    c = c%(2**i)
    r = r%(2**i)
ans = 0
for i in range(n):
    if x[i] + y[i] == 2:
        ans += 3*(4**(n-1-i))
    elif x[i] == 1:
        ans += (4**(n-1-i))
    elif y[i] == 1:
        ans += 2*(4**(n-1-i))
    
print(ans)



'''
recursion 방법

import sys
# input = sys.stdin.readline

n,r,c  = map(int, input().split())

ans= 0
dj = [0,1,0,1]
di = [0,0,1,1]

def Z(n,r,c,cnt):
    if n == 1:
        for d in range(4):
            if r ==  di[d] and c == dj[d]:
                print(cnt + d)              
                

    else: 
        a = c//(2**(n-1)) + 2*(r//(2**(n-1)))
        Z(n-1, r%(2**(n-1)), c%(2**(n-1)), cnt+a*(4**(n-1)))


Z(n,r,c,0)
'''