import sys

if len(sys.argv) < 2: 
    exit("Usage: {} FILENAME".format(sys.argv[0]))

filename = sys.argv[1]

#Read line by line by getting numbers
total1 = 0
evenCount = 0   # can be divided by 2
oddCount = 0    # cannot be divided by 2
SumofOdd = 0
with open(filename) as fh:
    for line in fh:
        number = int(line)
        if number % 2 == 0 :
            total1 += int(line)
            evenCount = evenCount + 1
        elif number % 2 != 0:
            oddCount = oddCount + 1
            SumofOdd += int(line)


print('The total of All Even numbers', evenCount , ' The Sum is :', total1)
print('The total of All Odd numbers', oddCount, ' The Sum is :', SumofOdd )

# Another way of solving the problem

#with open(filename) as fh:
   # total2 = sum(map(int, fh.readlines()))

#print(total2)    

