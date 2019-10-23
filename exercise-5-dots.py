for i in range(15):
    if i <= 5:
        print('* ' * i)
    elif i <= 9:
        print('* ' * (10 - i))
    else:
        print('* ' * (15 - i))
