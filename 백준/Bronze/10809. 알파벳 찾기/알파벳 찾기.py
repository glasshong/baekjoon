s = input()
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
f = []
for i in range(len(l)):
    if l[i] in s:
        f.append(s.index(l[i]))
    else:
        f.append(-1)
print(*f)