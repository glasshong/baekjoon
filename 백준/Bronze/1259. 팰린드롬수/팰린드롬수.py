while True:
    n = input()
    if int(n) != 0:
        if int(n) == int(n[::-1]):
            print('yes')
        else:
            print('no')
    else:
        break