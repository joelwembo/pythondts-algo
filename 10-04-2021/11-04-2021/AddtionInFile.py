import sys

if len(sys.argv) < 2: 
    exit("Usage: {} FILENAME".format(sys.argv[0]))

filename = sys.argv[1]

#Read line by line by getting numbers
total1 = 0
with open(filename) as fh:
    for line in fh:
        for i in line:    #check each for numbers only
            if i.isdigit() == True:
                total1 += int(line)
            else:
                pass   

print(total1)

# Another way of solving the problem

#with open(filename) as fh:
   # total2 = sum(map(int, fh.readlines()))

#print(total2)    

