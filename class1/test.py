def dijkstra(start, adj1):
    # 각 노드로 가는 비용이 싼 노드들을 하나씩 선택하면서, 갈수 있는 경로가 있고, 비용이 기존 경로보다
    # 더 싸면 업데이트 해주기
    # start에서 각 노드로 가는 비용
    distance = adj1[start][:]
    # 이미 선택한 정점을 표시하기위한 리스트
    visited = [0]*(N**2)
    visited[start] = 1
    distance[start] = 0
    while sum(visited) <= (N**2)-1:
        min_idx = 0
        min_val = 0xffffff
        for i in range(N**2):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        # 최소 비용을 가지는 노드를 안다!
        visited[min_idx] = 1
        # 방금 선택된 노드를 거쳐서 갈 수 있는 노드들의 방문비용 확인
        for i in range(N**2):
            if not visited[i] and distance[i] > min_val + adj1[min_idx][i]:
                distance[i] = min_val + adj1[min_idx][i]
    return distance


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    adj1 = [[0xffffff]*(N**2) for _ in range(N**2)]

    # (이동 전 인덱스, 이동 후 인덱스, 연료소비량) 담을 리스트

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(N):
        for j in range(N):
            # 상하좌우 이동 가능한 노드와 연료 graph에 추가
            for x in range(4):
                di = i + d[x][0]
                dj = j + d[x][1]

                if 0 <= di < N and 0 <= dj < N:
                    if data[di][dj] <= data[i][j]:  # 도착지가
                        adj1[N*i+j][N*di+dj] = 1
                    else:
                        adj1[N*i+j][N*di+dj] = (data[di][dj] - data[i][j])+1

    result = dijkstra(0, adj1)
    print(f'#{tc} {result[-1]}')