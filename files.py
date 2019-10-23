file_name = 'example.txt'

try:
    fsock = open(file_name)
except IOError:
    print('The file does not exist.')
