import sys

input = sys.stdin.read
output = sys.stdin.write

K, N, *lanline_list = list(map(int, input().split())) 

# min_lanline = min(lanline_list)
# ans = min_lanline
# lanline_count = sum([x//ans for x in lanline_list])

# if lanline_count> N:
#     while lanline_count > N:
#         ans +=1
#         lanline_count = 0
#         for i in lanline_list:
#             lanline_count += i//ans
#         if lanline_count < N:
#             ans -=1
# else:
#     while lanline_count < N:
#         ans -=1
#         lanline_count = 0
#         for i in lanline_list:
#             lanline_count += i//ans    무조건 시간초과... 이분 탐색을 사용해야 할 듯 하다.

start =0
end = max(lanline_list)

while start <= end:
    mid = (start+end)//2

    lanline_count = 0
    for i in lanline_list:
        lanline_count += i//mid
    
    if lanline_count >= N:
        start = mid +1
    else :
        end = mid -1

print(end)