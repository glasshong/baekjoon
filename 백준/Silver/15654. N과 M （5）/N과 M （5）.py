N, M = map(int, input().split())
l = list(map(int, input().split()))
ls = sorted(l)
k = []

def dfs(s):
    if len(k) == M:
        print(' '.join(map(str, k)))
        return
    
    for i in ls:
        if i not in k:
            k.append(i)
            dfs(i)
            k.pop()

dfs(min(ls))