import sys
input = sys.stdin.readline
import heapq

N = int(input())

heap = []

for i in range(N):
    a = int(input())
    if a == 0:
        heapq.heappop(heap)
        