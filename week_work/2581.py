m = int(input())
n = int(input())

visited = [False]*10001
visited[1] = True
for i in range(2,10001):
    if visited[i] == False:
        j = 2
        while j*i < 10001:
            visited[j*i] = True
            j += 1

sum = 0
min = 0
for i in range(n,m-1, -1):
    if visited[i] == False:
        sum += i
        min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)