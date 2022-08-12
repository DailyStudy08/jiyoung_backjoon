import sys
from collections import deque
import math


# input = sys.stdin.readline
f = open('input.txt','r')
input = f.readline

visited = [False]* 101
n, m = map(int, input().split())
ladder_lst = [list(map(int, input().split())) for _ in range(n)]
snake_lst = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(101)]

for i in range(1,100):
    graph[i].append(i+1)

for coord in ladder_lst:
    graph[coord[0]].append(coord[1])

for coord in snake_lst:
    graph[coord[0]].append(coord[1])


def bfs(v):
        q = deque()

        q.append(v) 
        visited[v] = True 
        cnt = 0
        while q:
            v = q.popleft()

            print(v, end= ' ') 
            # if v == 100:
            #     print(int(math.ceil(cnt/6)))
            #     break
            adj_v = graph[v] 
            for u in adj_v: 
                if not visited[u]:
                    cnt += 1
                    q.append(u)
                    visited[u] = True

bfs(1)


