class PersonBase:
    def __init__(self, surname='Doe'):
        self.surname = surname


class Person(PersonBase):                     # inheritance
    ('The class represents person data.')

    def __init__(self, name='Nick', age=20):  # constructor
        PersonBase.__init__(self, surname='Doe')
        self.name = name                      # no need to create fields separately
        self.age = age

    def get_person_data(self):
        return 'Hello! My name is %s %s. And I\'m %s years old.' % (self.name, self.surname, self.age)\


    @staticmethod
    def get_person_data_static(self):
        return 'Hello! My name is %s %s. And I\'m %s years old.' % (self.name, self.surname, self.age)

    def __cmp__(self, other):
        if self.age > other.age:
            return self.name
        elif self.age < other.age:
            return other.name
        else:
            return False


john = Person('John')
print('Dynamic: %s' % john.get_person_data())
print('Static: %s' % Person.get_person_data_static(john))
print(john.__doc__)

jeff = Person('Jeff', 35)

result = Person.__cmp__(john, jeff)
if result:
    print('%s is older.' % result)
else:
    print('%s and %s are of the same age' % (john.name, jeff.name))

# adding a method to the class


def sing(self):
    return 'La-la-la!'


Person.sing = sing
print(john.sing())
