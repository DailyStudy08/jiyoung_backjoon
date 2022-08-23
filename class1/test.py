adj_lst = [[[] for x in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        adj_lst[i][j].append(i+j)

print(adj_lst)
