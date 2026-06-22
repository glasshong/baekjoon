def solution(arr):
    a = []
    for i, j in enumerate(arr):
        if j == 2:
            a.append(i)
    if len(a) > 2:
        return arr[a[0]:a[-1]+1]
    elif len(a) == 2:
        return arr[a[0]:a[1]+1]
    elif len(a) == 1:
        return [arr[a[0]]]
    else:
        return [-1]