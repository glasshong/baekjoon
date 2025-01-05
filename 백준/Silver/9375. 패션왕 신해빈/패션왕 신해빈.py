import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
		d = {}
		n = int(input().strip())
		for _ in range(n):
				v, k = input().strip().split()
				if k in d:
						d[k].append(v)
				else:
						d[k] = [v]

		c = 1
		for x in d:
				c *= (len(d[x])+1)
		print(c-1)