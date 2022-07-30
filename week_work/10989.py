import sys


N = int(sys.stdin.readline())

int_list = [0]*10001
for i in range(N):
    int_list[int(sys.stdin.readline())] += 1


for i in range(10001):
    if int_list[i]:
        for a in range(int_list[i]):
            print(i)