while True:
    try:
        a, b, c = map(int, input().split())
        l = max(b-a, c-b)
        print(l-1)
    except:
        exit()