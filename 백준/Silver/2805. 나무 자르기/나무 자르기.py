import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

low, high = 0, max(l)
answer = 0

while low <= high:
    mid = (low + high) // 2
    total = sum(i-mid for i in l if i > mid)

    if total >= m:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)