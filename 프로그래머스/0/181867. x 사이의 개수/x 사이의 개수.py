def solution(myString):
    a = myString.split('x')
    answer = []
    for i in a:
        answer.append(len(i))
    return answer