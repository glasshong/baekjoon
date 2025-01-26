l = int(input())
s = input()

d = {}
p = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1, 27):
    d[p[i-1]] = i

t = 0
for j in range(l):
    t += d[s[j]] * (31 ** j)

print(t % 1234567891)