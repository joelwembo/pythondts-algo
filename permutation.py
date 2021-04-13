def permutationFunction(n):
    if (n <= 1):
        return 1
    else:
        return n * permutationFunction(n-1)

count = 10
while count >= 10:
    print(permutationFunction(count))
    count = count -1
