import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def topology_sort():
    q = deque()
    ans_lst = []

    for i in range(1,n+1):
        if degree[i] == 0:
            q.append(i)
    
    if len(q) >1 or len(q) == 0:
        return 'IMPOSSIBLE'
    
    for i in range(1,n+1):
        if not q:
            return 'IMPOSSIBLE'
        
        cur = q.popleft()
        ans_lst.append(cur)

        for adj in graph[cur]:
            degree[adj] -= 1
            if degree[adj] == 0:
                q.append(adj)
    
    return ans_lst



for tc in range(1,T+1):
    n = int(input())
    last_year_rank = list(map(int, input().split()))
    m = int(input())
    graph = [[] for _ in range(n+1)]
    degree = [0]*(n+1)

    for i in range(n):
        for j in range(i+1,n):
            graph[last_year_rank[i]].append(last_year_rank[j])
            degree[last_year_rank[j]] += 1 

    
    for i in range(m):
        a,b = map(int, input().split())
        for j in graph[a]:
            if j == b:
                graph[b].append(a)
                graph[a].remove(b)
                degree[a] += 1
                degree[b] += -1
                break
        else:
            graph[a].append(b)
            graph[b].remove(a)
            degree[a] -= 1
            degree[b] += 1

    
        
    
    ans = topology_sort()

    if ans == 'IMPOSSIBLE' or ans == '?':
        print(ans)
    else:
        print(*ans)
