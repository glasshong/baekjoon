from collections import deque

def solution(numbers, k):
    d = deque(numbers)
    i = 1
    while i != k:
        d.rotate(-2)
        i += 1
    answer = list(d)
    return answer[0]