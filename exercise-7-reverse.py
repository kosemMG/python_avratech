number = input('Please, input 3-digital number to be reversed: ')


def validate(num):
    abs_num = abs(num / 100)
    if abs_num >= 10 or abs_num < 1:
        return False
    return True


def reverse(num):
    return (num % 10) * 100 + abs(num % 100 / 10) * 10 + abs(num / 100)


if validate(number):
    result = reverse(number)
else:
    result = 'Wrong input!'

print(result)

