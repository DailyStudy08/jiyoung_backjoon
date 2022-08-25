from datetime import datetime
import sys
start = datetime.now()
f = open('input.txt', 'r')
input = f.read
# input = f.readline


m,n,b, *ground = list(map(int,input().split()))
# m,n,b = map(int, input().split())
# ground = [list(map(int, input().split())) for _ in range(m)]
print(ground)
end = datetime.now()

elapsed_time = end - start
print(elapsed_time)