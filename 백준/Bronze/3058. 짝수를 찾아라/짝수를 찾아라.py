for _ in range(int(input())):
    l = list(map(int, input().split()))
    e = []
    for i in l:
        if i % 2 == 0:
            e.append(i)
    print(sum(e), min(e))