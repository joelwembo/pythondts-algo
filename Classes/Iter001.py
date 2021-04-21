def first_n(n):
    '''Build and return a list'''
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


sum_of_first_n = sum(first_n(1000000))

print(sum_of_first_n)