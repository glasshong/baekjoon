N, K = map(int, input().split())
s = set()
for _ in range(N):
    a = int(input())
    s.add(a)
l = sorted(list(s), reverse=True)
n = 0
for i in l:
    if i <= K:
        n += K // i
        K = K % i
print(n)