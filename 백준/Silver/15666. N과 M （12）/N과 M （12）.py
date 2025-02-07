N, M = map(int, input().split())
l = list(map(int, input().split()))
ls = sorted(list(set(l)))
k = []

def dfs(start):
    if len(k) == M:
        if M == 1:
            print(' '.join(map(str, k)))
        else:
            t = 0
            for i in range(1, len(k)):
                if k[i] >= k[i-1]:
                    t += 1
                else:
                    break
            if t == len(k)-1:
                print(' '.join(map(str, k)))
        return

    for i in ls:
        k.append(i)
        dfs(i)
        k.pop()
        
dfs(ls)