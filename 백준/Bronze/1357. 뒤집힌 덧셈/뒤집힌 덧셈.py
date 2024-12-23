X, Y = map(str, input().split())
sum = int(X[::-1]) + int(Y[::-1])
print(int(str(sum)[::-1]))