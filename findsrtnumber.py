

# Python program to find a non-negative interger

def integer_square_root(n):

    low = 0
    high = n

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if (mid_squared <= n) :
            low = mid + 1
        else:
            high = mid - 1    
    return low - 1        
    

print('Program Starting...')
print('please enter an non-negative integer:    ')
inputData = int(input())

print(integer_square_root(inputData))
