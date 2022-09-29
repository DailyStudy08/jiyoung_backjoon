import sys
input = sys.stdin.readline

v,e = map(int, input().split())
adj_lst = []
rep = [i for i in range(v+1)]
def Union(x,y):
    rep[Find_set(y)] = Find_set(x)
    
def Find_set(x):
    if x == rep[x]:
        return x
    else:
        return Find_set(rep[x])

for i in range(e):
    a,b,c, =map(int, input().split())
    adj_lst.append((a,b,c))

adj_lst = sorted(adj_lst, key=lambda x : x[2])
weight_sum = 0
A = set()

for i in range(e):
    a,b,c, = adj_lst[i]
    if Find_set(a) != Find_set(b):
        weight_sum += c
        Union(a,b)

print(weight_sum)


