def fibfunction(n):
    if(n <=2):
        return 1
    else:
        return fibfunction(n-1) + fibfunction(n-2)


print(fibfunction(7))
count = 5
while count != 0:
    print("Please Enter Number")
    x =int(input())
    print(fibfunction(x))
    count = count-1
    if count == 0:
        print("Program Terminated")
    
