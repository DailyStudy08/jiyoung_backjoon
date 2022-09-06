from heapq import heappop, heappush
n, k = map(int, input().split())

adj_lst = [[(i-1,1), (i+1,1), (2*i, 0)] for i in range(100001)]
INF = 1000000


time_lst = [INF]*(100001)


def dijkstra(start):
    q = []
    heappush(q, (0,start))

    while q:
        now = heappop(q)
        current_time = now[0]

        if current_time > time_lst[now[1]]:
            continue

        for i in adj_lst[now[1]]:
            if i[0] <0 or i[0] >100000:
                continue

            time = current_time + i[1]
            if time_lst[i[0]] > time:
                time_lst[i[0]] = time
                heappush(q, (time, i[0]))

time_lst[n] = 0

dijkstra(n)

print(time_lst[k])

