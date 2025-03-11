n = int(input())
a = 1000-n

count = 0
coin_types = [500, 100, 50, 10, 5, 1]

for i in coin_types:
    count += a // i
    a -= i * (a // i)

print(count)