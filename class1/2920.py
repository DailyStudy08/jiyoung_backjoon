import sys
input = sys.stdin.readline

ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]
in_play = list(map(int, input().split()))

if in_play== ascending:
    print('ascending')
elif in_play == descending:
    print('descending')
else:
    print('mixed')