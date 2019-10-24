class Operation:
    def __init__(self, input_obj):
        self.arg1 = input_obj.arg1
        self.arg2 = input_obj.arg2


class Add(Operation):
    def __init__(self, input_obj):
        Operation.__init__(self, input_obj)

    def run(self):
        return self.arg1 + self.arg2


class Subtract(Operation):
    def __init__(self, input_obj):
        Operation.__init__(self, input_obj)

    def run(self):
        return self.arg1 - self.arg2


class Multiply(Operation):
    def __init__(self, input_obj):
        Operation.__init__(self, input_obj)

    def run(self):
        return self.arg1 * self.arg2


class Divide(Operation):
    def __init__(self, input_obj):
        Operation.__init__(self, input_obj)

    def validate(self):
        if self.arg2 == 0:
            return False
        return True

    def run(self):
        if self.validate():
            return self.arg1 / self.arg2
        return 'Division by zero!'


class Input:
    def __init__(self, arg1, arg2, select):
        if self.validate(arg1, arg2, select):
            self.arg1 = int(arg1)
            self.arg2 = int(arg2)
            self.select = select
        else:
            exit('Wrong input!')

    @staticmethod
    def validate(arg1, arg2, select):
        if arg1.isdigit() and arg2.isdigit() and select in range(1, 5):
            return True
        else:
            return False


class Switch:
    def __init__(self):
        self.operation = {
            1: [Add, '+'],
            2: [Subtract, '-'],
            3: [Multiply, '*'],
            4: [Divide, '/']
        }


inputObj = Input(
    raw_input('Input the first argument: '),
    raw_input('Input the second argument: '),
    input('Select operation: ')
)

OperationClass = Switch().operation[inputObj.select][0]

result = OperationClass(inputObj).run()

print(result)
