A, B = map(str, input().split())
print(max(int(A[2])*100 + int(A[1])*10 + int(A[0]), int(B[2])*100 + int(B[1])*10 + int(B[0])))