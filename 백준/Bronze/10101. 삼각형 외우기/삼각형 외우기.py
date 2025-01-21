t = []
for _ in range(3):
    t.append(int(input()))

if t[0] == t[1] == t[2] == 60:
    print('Equilateral')
elif t[0] + t[1] + t[2] == 180:
    if t[0] == t[1] or t[0] == t[2] or t[1] == t[2]:
        print('Isosceles')
    else:
        print('Scalene')  
else:
    print('Error')