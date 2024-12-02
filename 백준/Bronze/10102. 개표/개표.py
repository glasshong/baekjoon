V = int(input())
l = list(input())

A = l.count('A')
B = l.count('B')

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')