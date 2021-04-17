

print('Enter information here: ---->')
inputData = input()

with open('data.txt', 'a') as a_writer:
    a_writer.write(inputData)

with open('data.txt', 'r') as reader:
    print(reader.read())    

