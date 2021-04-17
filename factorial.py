# Program to demonstrate a factorial function

def factorial(n):
    assert n >= 0,  "Factorial is not defined for Zero or negative numbers"

    if ( n < 2 ):
        return 1
    else: 
        return n * factorial(n-1)   

print(factorial(120))