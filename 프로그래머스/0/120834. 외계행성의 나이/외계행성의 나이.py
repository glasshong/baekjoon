def solution(age):
    p = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    x = age // 100 
    y = (age - (x * 100)) // 10
    z = age - (x * 100 + y * 10)
    if age == 1000:
        final_age = ['b', 'a', 'a', 'a']
    elif age >= 100:
        final_age = [p[x], p[y], p[z]]
    elif age >= 10:
        final_age = [p[y], p[z]]
    else:
        final_age = [p[z]]
    return "".join(final_age) 