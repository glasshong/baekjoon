n, m = map(int, input().split())

s = n if n < m else m

for i in range(s, 0, -1):
    if n % i == 0 and m % i == 0:
        print(i)
        break

print(n // i * m)