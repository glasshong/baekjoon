def fibonacci(max_n):
		fib = [0] * (max_n+1)
		fib[0] = 1
		fib[1] = 1
		for i in range(2, max_n+1):
				fib[i] = fib[i-1] + fib[i-2]
		return fib

max_n = 45
fib_seq = fibonacci(max_n)

n = int(input())
for _ in range(n):
		x = int(input())
		print(fib_seq[x])