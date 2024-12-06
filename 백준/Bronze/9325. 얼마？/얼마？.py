T = int(input())
for _ in range(T):
    s = int(input())
    n = int(input())
    a = 0
    for _ in range(n):
        q, p = map(int, input().split())
        a += q * p
    print(s+a)