import sys
from heapq import heappush, heappop

input = sys.stdin.readline
T = int(input())

for i in range(1,T+1):
    min_heap = []
    max_heap = []
    i_cnt = 0
    d_cnt = 0
    n = int(input())
    for j in range(n):
        query = input().split()
        if query[0] == 'I':
            i_cnt += 1
            heappush(min_heap, int(query[1]))
            heappush(max_heap, -int(query[1]))
        elif query[0] == 'D':
            d_cnt += 1
            if d_cnt <= i_cnt:
                if query[1] == '1':
                    heappop(max_heap)
                else :
                    heappop(min_heap)
            print(min_heap)
            print(max_heap)
                   
    
    if d_cnt< i_cnt:
        print(min_heap[0], -max_heap[0])
    else:
        print('EMPTY')
        
       
        
