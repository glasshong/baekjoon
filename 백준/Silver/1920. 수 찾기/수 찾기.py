N = int(input())
l_N = set(map(int, input().split()))
M = int(input())
l_M = list(map(int, input().split()))
for i in l_M:
    if i in l_N: 
        print(1)
    else:
        print(0)