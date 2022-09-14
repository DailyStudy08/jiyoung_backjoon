import sys
input = sys.stdin.readline

T = int(input())
def bellman_ford(start):
    
    distance[start] = 0

    for i in range(n):
        for j in range(2*m+w):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]

            if  distance[next_node]> distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == n-1:
                    return True
    
    return False


for tc in range(T):
    n, m , w  = map(int, input().split())
    edges = []
    INF = 12500*10000
    distance = [INF] *(n+1)
    for i in range(m):
        s, e, t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    
    for i in range(w):
        s,e,t = map(int, input().split())
        edges.append((s,e,-t))

    if bellman_ford(i):
        print('YES')  
    else:
        print('NO')
    
