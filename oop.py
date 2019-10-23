class Person:
    ('The class represents person data.')

    surname = 'Doe'

    def __init__(self, name='Nick', age=20):  # constructor
        self.name = name                      # no need to create fields separately
        self.age = age

    def get_person_data(self):
        return 'Hello! My name is %s %s. And I\'m %s years old.' % (self.name, self.surname, self.age)\


    @staticmethod
    def get_person_data_static(self):
        return 'Hello! My name is %s %s. And I\'m %s years old.' % (self.name, self.surname, self.age)


john = Person('John')
print('Dynamic: %s' % john.get_person_data())
print('Static: %s' % Person.get_person_data_static(john))
print(john.__doc__)
