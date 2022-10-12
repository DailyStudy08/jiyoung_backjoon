exp = '100-200*300-500+20'

exp = exp.split('+')

for i in range(len(exp)):
    exp[i] = exp[i].split('-')
    for j in range(len(exp[i])):
        exp[i][j] = exp[i][j].split('*')


for i in range(len(exp)):
    for j in range(len(exp[i])):
        num_tmp = int(exp[i][j][0])
        for k in range(1,len(exp[i][j])):
            num_tmp *= int(exp[i][j][k])
        exp[i][j] = num_tmp

for i in range(len(exp)):
    num_tmp = int(exp[i][0])
    for j in range(1,len(exp[i])):
        num_tmp -= int(exp[i][j])
    exp[i] = num_tmp

num_tmp = exp[0]
for i in range(1,len(exp)):
    num_tmp += exp[i]

exp = num_tmp


print(abs(exp))