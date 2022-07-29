
s = input().upper()
counted_array = [0]*26
for c in s:
    counted_array[ord(c) - ord('A')] += 1

cnt = 0
for idx, i in enumerate(counted_array):
    if cnt < i:
        a = idx + ord('A')
        print_c = chr(a)
        cnt = i
    elif cnt == i:
        print_c = '?'

print(print_c)