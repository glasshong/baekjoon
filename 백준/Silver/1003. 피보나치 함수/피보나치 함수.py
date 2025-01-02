def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return 1, 0
    else:
        for i in range(n-1):
            a, b = b, a+b
        return a, b   

T = int(input())
for i in range(T):
    N = int(input())
    a, b = fibonacci(N)
    print(a, b)