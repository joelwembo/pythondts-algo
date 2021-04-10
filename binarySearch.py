#Python Program to demonstrate Binary Search

def binarySearch(theValues, target):
    # Start with the entire sequence of elements
    low = 0
    high = len(theValues) - 1

    # Repeatedly subdivide the sequence in half using this while loop
    while low <= high:
        # Find the midpoint of the sequence
        mid = (high + low) // 2
        # Does the midpojnt contain the target ?
        if theValues[mid] == target:
            return True
        # Or does the target precede the midpoint ?
        elif target < theValues[mid]:
            high = mid - 1
        # Or does it follow the midpoint ?
        else:
            low = mid + 1     
    # If the sequence cannot be sudivided further, we are done
    return False  

myarray = [1,2,3,4,5,6,7,80]
print(binarySearch(myarray,80))        

