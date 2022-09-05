import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(cur):
    tmp_sum = 0
    first_max = 0
    second_max = 0
    for i in adj_lst[cur]:
        if not visited[i[0]]:
            visited[i[0]] = True
            dfs(i[0])
            r_dp[cur] = max(r_dp[cur], r_dp[i[0]]+ i[1])
            if first_max:
                if r_dp[i[0]]+ i[1] > first_max:
                    first_max, second_max = r_dp[i[0]]+ i[1] , first_max
                elif r_dp[i[0]]+ i[1] >second_max:
                    second_max = r_dp[i[0]]+ i[1]
            else:
                first_max = r_dp[i[0]]+ i[1]

    tmp_sum = first_max + second_max

    global r
    if r < tmp_sum:
        r = tmp_sum


n = int(input())
adj_lst = [[] for _ in range(n+1)]


for i in range(n-1):
    a,b,c = map(int, input().split())
    adj_lst[a].append([b,c])


r = 0
r_dp = [0]*(n+1)
visited = [False]*(n+1)
dfs(1)

         
print(r)
