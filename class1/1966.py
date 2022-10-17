import sys

input = sys.stdin.readline
T = int(input())

for tc in range(1,T+1):
    n, m = map(int, input().split())
    print_lst = list(map(int, input().split()))
    q = []

    for i in range(n):
        q.append((print_lst[i], i == m))
            
    cnt = 1

    while True:
        a = max(q)
        cur = q.pop(0)
        if cur[0] == a[0]:
            if cur[1]:
                print(cnt)
                break

            cnt += 1
        else:
            q.append(cur)

