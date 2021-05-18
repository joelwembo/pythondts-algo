
mydata = [12,4,5,10,7]
target = 14

def linearSearch(arr, x):
    for i in range(len(arr)):
        if (arr[i] == x ):
            return 'The element is found on:  ', i
    return 'Not Found'

def bubbleSort(list):
    for iter_num in range(len(list) -1, 0 , -1):
        for idx in range(iter_num):
            if (list[idx] > list[idx + 1]):
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp



#print(linearSearch(mydata, target))

print(bubbleSort(mydata))