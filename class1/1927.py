from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    a = int(input())
    if a == 0:
        if q:
            print(heappop(q))
        else:
            print(0)
    else:
        heappush(q,a)
