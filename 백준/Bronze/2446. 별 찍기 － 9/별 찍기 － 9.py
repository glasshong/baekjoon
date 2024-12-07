N = int(input())
for i in range(1, N):
	print(' ' * (i-1) + '*' * (2*(N-i)+1))
for j in range(1, N+1):
    print(' ' * (N-j) + '*' * (2*j-1))