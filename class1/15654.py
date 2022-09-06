import sys
input = sys.stdin.readline
n, m, = map(int, input().split())
num_lst = list(map(int, input().split())) 

num_lst.sort()
visited = [False]*n

def backtrack(depth , print_index):
    if depth == m:
        for i in print_index:
            print(num_lst[i], end=' ')
        print()
        return

    for i in range(0, n):
        if not visited[i]:
            visited[i] = True
            backtrack(depth+1, print_index + [i])
            visited[i] = False
        

backtrack(0,[])