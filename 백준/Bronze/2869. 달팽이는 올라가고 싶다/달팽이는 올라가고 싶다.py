import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

if v == a:
    print(1)
elif v % (a-b) <= b:
    if ((v-a) % (a-b)) == 0:
        print((v-a) // (a-b) + 1)
    else:
        print((v-a) // (a-b) + 2)
else:
    print(v // (a-b) + 1)