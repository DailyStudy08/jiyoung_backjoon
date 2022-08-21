import sys
from collections import deque
# input = sys.stdin.readline


n,k = map(int, input().split())

adj_lst = [[] for _ in range(100001)]
adj_lst[0] = [1]

for i in range(1,100001):
    adj_lst[i].append(i-1)
    adj_lst[i].append(i+1)
    adj_lst[i].append(2*i)

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