import sys
from collections import deque

input = sys.stdin.readline

T= int(input())

for tc in range(T):
    n, k = map(int, input().split())
    t_n = [0] + list(map(int, input().split()))
    dp = [[] for _ in range(n+1)]
    degree = [0]*(n+1)
    for i in range(k):
        a,b = map(int, input().split())
        dp[a].append(b)
        degree[b] += 1

    w = int(input())
    q = deque()
    real_dp = [0]*(n+1)

    for i in range(1,n+1):
        if degree[i] == 0:
            q.append(i)
            real_dp[i] = t_n[i]

    while q:
        cur = q.popleft()

        if cur == w:
            break

        for i in dp[cur]:
            degree[i] -= 1
            real_dp[i] = max(real_dp[cur] + t_n[i] , real_dp[i])
            if degree[i] == 0:
                q.append(i)
                
    

    time_sum = real_dp[w]

    
    print(time_sum)
