n, m = map(int, input().split())
tree_lst = list(map(int, input().split()))

low = 1
high = 1000000000

middle = (low+ high)//2
answer = 0

while low <= high:
    sum_tree = 0
    for i in range(n):
        a = tree_lst[i] - middle
        if a>0:
            sum_tree += a

    if sum_tree == m:
        answer = middle
        break

    elif sum_tree < m:
        high = middle -1
        middle = (low+ high)//2
    elif sum_tree > m:
        low = middle +1
        middle = (low+high)//2

print(middle)