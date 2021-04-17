

try:
    file = open('data.txt')
    print(file.read())

finally:
    print('file not available or not authorized to open this type of file')

