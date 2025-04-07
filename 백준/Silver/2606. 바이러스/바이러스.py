c = int(input())
n = int(input())

graph = [[] for _ in range(c+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = [False] * (c+1)

count = 0
def dfs(i):
    global count
    v[i] = True
    for j in graph[i]:
        if not v[j]:
            count += 1
            dfs(j)

dfs(1)
print(count)