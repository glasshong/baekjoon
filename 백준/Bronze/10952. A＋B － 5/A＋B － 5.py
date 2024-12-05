import sys

for i in sys.stdin:
    A, B = map(int, i.split())
    if A == 0 & B == 0:
        break
    else:
        print(A + B)