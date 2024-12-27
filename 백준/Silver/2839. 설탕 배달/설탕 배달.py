import sys
N = int(sys.stdin.readline())
if (N == 1) | (N == 2) | (N == 4) | (N == 7):
    print(-1)
elif N % 5 == 0:
    print(N // 5)
elif (N % 5 == 1) | (N % 5 == 3):
    print(N // 5 + 1)
else:
    print(N // 5 + 2)