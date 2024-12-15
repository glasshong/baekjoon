for _ in range(int(input())):
    P, M = map(int, input().split())
    l = []
    for _ in range(P):
        l.append(int(input()))
    print(len(l) - len(set(l)))