import sys
input = sys.stdin.readline

t = int(input())

def dfs(i):
    v[i] = True
    for j in graph[i]:
        if not v[j]:
            dfs(j)
 
for _ in range(t):
    n = int(input())
    lst1 = list(range(1, n+1))
    lst2 = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    for i in range(n):
        graph[lst1[i]].append(lst2[i])
        graph[lst2[i]].append(lst1[i])
    
    v = [False] * (n+1)
    
    count = 0
    for i in range(1, n+1):
        if not v[i]:
            dfs(i)
            count += 1
    
    print(count)