T = int(input())
for _ in range(T):
    N = int(input())
    dic = {}
    for _ in range(N):
        S, L = input().split()
        dic[S] = int(L)
    print(max(dic, key=dic.get))