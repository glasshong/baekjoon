n = int(input())
for _ in range(n):
    p = int(input())
    dic = {}
    for _ in range(p):
        v, k = input().split()
        dic[k] = int(v) 
    print(max(dic, key=dic.get)) 