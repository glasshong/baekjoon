import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n
b = list(map(int, input().split()))

count = 0
while True:
    if a == b:
        break
    else:
        if all(i % 2 == 0 for i in b):
            for i in range(n):
                b[i] = b[i] // 2
            count += 1
        else:
            for i in range(n):
                if b[i] % 2 == 1:
                    b[i] = b[i] - 1
                    count += 1

print(count)