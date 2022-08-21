import sys
from heapq import heappush, heappop

input = sys.stdin.readline
T = int(input())

for i in range(1,T+1):
    min_heap = []
    max_heap = []
    i_cnt = 0

    n = int(input())
    visited = [False]*(n+1)
    for j in range(n):
        query = input().split()
        if query[0] == 'I':
            i_cnt += 1
            heappush(min_heap, (int(query[1]), i_cnt))
            heappush(max_heap, (-int(query[1]), i_cnt))
            visited[i_cnt] = True
        elif query[0] == 'D':
            if query[1] == '1':
                while max_heap and visited[max_heap[0][1]] == False:
                    heappop(max_heap)
                if max_heap:
                    a = heappop(max_heap)
                    visited[a[1]] = False
            else :
                while min_heap and visited[min_heap[0][1]] == False:
                    heappop(min_heap)
                if min_heap:
                    a = heappop(min_heap)
                    visited[a[1]] = False


    while min_heap and visited[min_heap[0][1]] == False:
        heappop(min_heap)
    while max_heap and visited[max_heap[0][1]] == False:
        heappop(max_heap)
    
    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
        
       
        
