def linearSearch(theValues, target):
    n = len(theValues)
    for i in range( n ):
        # if the target is in the  ith element, return true
        if (theValues[i] == target):
            return True
    return False   

def sortedLinearSearch(theValues, item):
    n = len(theValues)
    for i in range(n):
        # if the target is found in.datetime A combination of a date and a time. Attributes: ()
        if (theValues == item):
            return True
        elif (theValues[i] > item):
            return False
    return False  


