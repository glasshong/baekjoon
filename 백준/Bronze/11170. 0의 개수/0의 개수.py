T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    zero = 0
    for i in range(N, M+1):
        if '0' in str(i):
            zero += str(i).count('0')
    print(zero)