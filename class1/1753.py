import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heappush(q,(0,start))
    current_dist = 0
    dist[start] = 0

    while q:
        now = heappop(q)
        current_dist = now[0]

        if current_dist > dist[now[1]]:
            continue

        for next in graph[now[1]]:
            distance = current_dist + next[1]
            if distance < dist[next[0]]:
                dist[next[0]] = distance
                heappush(q,(distance, next[0]))


v,e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e10)
dist = [INF]*(v+1)

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))


dijkstra(start)

for i in range(1,v+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
