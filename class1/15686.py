n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
store_list = []
home_list = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            store_list.append((i,j))
        if mat[i][j] == 1:
            home_list.append((i,j))

import itertools

combi = itertools.combinations(range(len(store_list)), m)


# 조합 구현 연습해보려다가 말음
# def cmton(arr, m):
#     a


def cal_score(store, homes):
    total_score = 0

    for home in homes:
        tmp_score = 100
        for st in store:
            if tmp_score > abs(st[0]-home[0]) + abs(st[1]- home[1]):
                tmp_score = abs(st[0]-home[0]) + abs(st[1]- home[1])
        
        total_score += tmp_score
    
    return total_score

answer = 1300


for comb in combi:
    can_store = []
    for index in comb:
        can_store.append(store_list[index])

    calculated_score = cal_score(can_store, home_list)

    if answer > calculated_score:
        answer = calculated_score

print(answer)


