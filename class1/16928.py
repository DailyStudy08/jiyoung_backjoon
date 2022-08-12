import sys
from collections import deque


input = sys.stdin.readline
# f = open('input.txt','r')
# input = f.readline

visited = [0]* 101
n, m = map(int, input().split())

graph = [0]*101
for i in range(1,101):
    graph[i] = i

for coord in range(n):
    a,b = map(int,input().split())
    graph[a] = b

for coord in range(m):
    a,b = map(int,input().split())
    graph[a]= b


def bfs(v):
        q = deque()
        q.append(v) 
        while q:
            v = q.popleft()
            for i in range(1,7):
                next = v + i
                if next > 100:
                    continue
                
                next = graph[next]

                if visited[next] == 0:
                    q.append(next)
                    visited[next] = visited[v] +1

                    if next == 100:
                        return
bfs(1)
print(visited[100])


