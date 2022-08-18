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