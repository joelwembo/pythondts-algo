# Searching the smallest value in the inter
def findSmallest( theValues):
    n = len(theValues)
    theList = []
    #Assume the first item is the smallest value
    smallestValue = theValues[0]
    # Determine if any other item in the sequence is sma
    for i in range(1 , n):
        if theList[i] < smallestValue:
            smallestValue = theValues[i]

    return smallestValue

myvalue = 10
print(findSmallest(myvalue))
