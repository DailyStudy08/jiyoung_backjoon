<<<<<<< HEAD
import sys
from collections import deque
# input = sys.stdin.readline


n,k = map(int, input().split())

adj_lst = [[] for _ in range(100001)]
adj_lst[0] = [1]

for i in range(1,100001):
=======
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
>>>>>>> ec550178e691be1a6705a5fafb3b71e48b9119bf
    adj_lst[i].append(i-1)
    adj_lst[i].append(i+1)
    adj_lst[i].append(2*i)

<<<<<<< HEAD
visited = [False]*100001
dp = [0]*100001

def bfs(start, end):
    q = deque([start])

    while q:
        cur = q.popleft()
        visited[cur] = True
        if cur == end:
            return dp[cur]
        for a in adj_lst[cur]:
            if a<100001 and visited[a] == False:
                q.append(a)
                dp[a] = dp[cur] +1
                visited[a] = True

print(bfs(n,k))                
=======
r, e = map(int,input().split())
print(BFS(r,e))




>>>>>>> ec550178e691be1a6705a5fafb3b71e48b9119bf
