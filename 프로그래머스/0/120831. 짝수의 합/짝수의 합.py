def solution(n):
    num = 1
    answer = 0
    while True:
        if num % 2 == 0:
            answer += num
        num += 1
        if num == n+1:
            break
    return answer
