import sys
input = sys.stdin.readline

parsing_minus = input().split('-')
result_value = []

for parsing in parsing_minus:

    tmp_plus = list(map(int, parsing.split('+')))
    sum_plus = 0

    for val in tmp_plus:
        sum_plus += val

    result_value.append(sum_plus) 

answer = 0
for result in result_value:
    answer -= result


answer += 2*result_value[0]
print(answer)