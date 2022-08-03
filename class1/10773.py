import sys
# input = sys.stdin.read
# output = sys.stdout.write
f =  open('input.txt', 'r')
input = f.readline

n = int(input())    # 느낌이 입력에서 잘만하면 2~3줄로도 풀 수 있을 것 같은데 정확하게 잘 모르겠네요.
lst = []
for i in range(n):
    m = int(input())
    if m== 0:
        lst.pop()
    else:
        lst.append(m)

print(sum(lst))

