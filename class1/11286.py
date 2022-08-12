import sys
input = sys.stdin.readline
import heapq

N = int(input())

heap = []

for i in range(N):
    a = int(input())
    if a == 0:
        if heap:
            pop_data = heapq.heappop(heap)
            print(pop_data[1])
        else:
            print('0')
    else:
        if a<0:
            heapq.heappush(heap, (abs(a)*2-1,a))
        else:
            heapq.heappush(heap, (abs(a)*2,a))
            
