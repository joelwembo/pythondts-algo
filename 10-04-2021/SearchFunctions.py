# Python Program to demonstrate Search Algorithms

def binarySearch(theValues, target) :
    low = 0
    high = len(theValues) - 1

    while low <= high:
        mid = (high + low) // 2
        if theValues[mid] == target :
            return True
        elif target < theValues[mid]:
            high = mid-1
        else:
            low = mid + 1

    return False

# sorts a sequence in ascending order using

def quickSort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

def bubbleSort(theSeq):
    n = len( theSeq )
    # Perform n-1 bubble operations on the sequence
    for i in range( n - 1 ) :
    # Bubble the largest item to the end
        for j in range(i + n -1) :
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp

    return theSeq

mylist = (10, 29, 100,7,89,12,3) 
myarray = [1, 21, 100,7,69,48,12]
a = 10
b = 12
c = 72
d = 1260
e = 100

print(binarySearch(mylist,4))
#print(bubbleSort(mylist))

print(quickSort(myarray))









