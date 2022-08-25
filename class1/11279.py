from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    cmd = int(input())
    if cmd:
        heappush(q, -cmd)
    else:
        if q:
            print(-heappop(q))
        else:
            print(0)

