#Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.


l = []
for i in range(2000, 3201):
    if(i%7 == 0) and (i%5 !=0):
        l.append(str(i))

           
#print(' ,'.join(l))      test   

# Factorial problem

def factorial(n): 
    if n == 0: 
        return 1
    return n * factorial(n - 1)  

y = int(input("Please enter an non null integer"))

print(',' , factorial(y) ) 






