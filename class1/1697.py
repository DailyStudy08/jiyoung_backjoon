from collections import deque

def BFS(root, end):
    visited[root] = True
    queue = deque([root])
    time = 0
    while queue:
        n = queue.popleft()
        time += 1
        for i in adj_lst[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                if i == end:
                    return time
            
visited = [False]*100001
adj_lst = [[] for _ in range(100001)]

for i in range(1,100000):
    adj_lst[i].append(i-1)
    adj_lst[i].append(i+1)
    adj_lst[i].append(2*i)

r, e = map(int,input().split())
print(BFS(r,e))




