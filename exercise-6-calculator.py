def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Division by zero!'


def run(arg1, arg2):
    return operation[choice][0](arg1, arg2)


operation = {
    1: [add, '+'],
    2: [subtract, '-'],
    3: [multiply, '*'],
    4: [divide, '/']
}

arg1 = input('Input the first argument: ')
arg2 = input('Input the second argument: ')
print('1. Add\n2. Subtract\n3. Multiply\n4. Divide')
choice = input('Select operation: ')

print('%s %s %s = %s' % (arg1, operation[choice][1], arg2, run(arg1, arg2)))

