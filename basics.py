# Types

name = 'moshe'
num = 3
other_num = 1.5

print(type(name))
print(type(num))
print(type(other_num))

# Comments

# single comment

'''
a lot of comments
'''

# Concatenation

uid = 'Role'
pwd = 'secret'
print('%s is not a good password for %s'%(pwd, uid))
print(pwd + ' is not a good password for ' + uid)   # both are correct

userCount = 6
print('Users connected: %s'%userCount)
# print('Users connected: ' + userCount) - ERROR!!! cannot concatenate 'str' and 'int' objects

# Operators

floor = 8.5 // 3
power = 3.14 ** 3
print(floor)
print(power)

# Strings methods

name = 'Danny'
print(name.upper())
print(name.lower())

print("Real Men Don't Apologize".replace("Apologize", "Eat Quiche"))

print('A bottle without a cork. ' * 4)

# Boolean variables

a = True
b = True
c = False
d = False

print(a and b)
print(a and c)
print(not a)
print((a and (not b)) or ((not a) and b))

# Blocks if, else, elif

if 2001 % 7 == 0:
    print('2001 is divisible by 71')     # must be 4 whitespaces
else:
    print('2001 is not divisible by 71') # must be 4 whitespaces

temp = 30
wind = 12

if temp > 25 and wind > 13:
    print('Go windsurfing!')
elif temp > 25 and wind <= 13:
    print('Go to the beach.')
    if temp > 30:
        print('Put your hat on.')
    else:
        print('Attend class...')

# Loops

n = 100
m = 100
while m > 0:
    if n % m == 0:
        print(m)
    m = m - 1

# range
print(range(6))
print(range(6, 12))
print(range(6, 12, 3))

partial_sum = 0
for i in range(1, 101):
    partial_sum = partial_sum + i
print(partial_sum)

# Arrays

my_list = [0, 1, 2, 3, 4]
print(my_list[-2])
print(len(my_list))

power_list = [i ** 2 for i in range(1, 11)]
print(power_list)

pa = 1
for k in power_list:
    pa = pa * k
print(pa)

char_list = ['a', 'b', 'c', 'd', 'e']
partial_list = char_list[1:3]
print(partial_list)

char_list.append('f')
print(char_list)

char_list.insert(2, 'n')
print(char_list)

char_list.extend(['g', 'h'])
print(char_list)

print(char_list.index('c'))

print('z' in char_list)

char_list.remove('n')
print(char_list)

# Tuples - arrays that cannot be changed.

t = ('a', 'b', 'c')
print(t.count('a'))
print(t.index('a'))

# Dictionaries

dictionary = {
    'Danny': 123,
    'Dana': 124,
    'Benny': 125
}

print(dictionary['Dana'])

dictionary['Shira'] = 456
print(dictionary)

# Functions

def func(x):
    return x * 3

print(func(3))

g = lambda x: x * 3
print(g(2))

g = lambda x, y: min(x ** 2 / y, y ** 2 / x)
print(g(2, 3))

def f(x):
    print(x)

f2 = f
print(f2('moshe'))
