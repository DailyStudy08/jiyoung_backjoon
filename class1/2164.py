from collections import deque
n = int(input())

lst = [x for x in range(1,n+1)]
cnt = 0
q = deque(lst)
while  q:
    if cnt%2 == 0:
        a = q.popleft()
    else:
        a = q.popleft()
        q.append(a)
    cnt += 1

print(a)