N, M = map(int, input().split())

l = []

def dfs(s):
	if len(l) == M:
		print(' '.join(map(str, l)))
		return
		
	for i in range(s, N+1):
		l.append(i)
		dfs(i)
		l.pop()

dfs(1)