len_s = int(input())
s = input()

count_2 = 0
count_e = 0
for i in range(len_s):
    if s[i] == '2':
        count_2 += 1
    else:
        count_e += 1

if count_2 > count_e:
    print(2)
elif count_2 < count_e:
    print('e')
else:
    print('yee')