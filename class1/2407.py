import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def fac(a):
    if a == 1:
        return 1
    
    return a*fac(a-1)

print(fac(n)//( fac(n-m)*fac(m)))
