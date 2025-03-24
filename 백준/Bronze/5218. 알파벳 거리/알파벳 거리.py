t = int(input())
for _ in range(t):
    w1, w2 = map(str, input().split())
    l = []
    for i in range(len(w1)):
        if w1[i] > w2[i]:
            l.append(ord(w2[i]) + 26 - ord(w1[i]))
        else:
            l.append(ord(w2[i]) - ord(w1[i]))
    print('Distances:', *l)