S = input()
l = []

for i in 'abcdefghijklmnopqrstuvwxyz':
    l.append(S.count(i))

print(*l)