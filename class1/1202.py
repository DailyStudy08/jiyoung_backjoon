# 입력부
import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
n, k = map(int, input().split())

worth_lst =[]
for i in range(n):
    m, v = map(int,input().split())
    heappush(worth_lst, (m,v))

can_pack_lst = []
for i in range(k):
    c = int(input())
    can_pack_lst.append(c)


can_pack_lst.sort()

ans = 0

tmp_lst = []

for i in range(k):
    while worth_lst and worth_lst[0][0] <= can_pack_lst[i]:
        a = heappop(worth_lst)
        heappush(tmp_lst, -a[1])
    
    if tmp_lst:
        ans += -heappop(tmp_lst)


print(ans)
    