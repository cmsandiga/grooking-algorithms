def binary_util(input, item, begin, end):
    mid  = int((begin + end) / 2)

    if begin > end:
        return None

    if input[mid] == item:
        return mid

    if item > input[mid]:
        return binary_util(input, item, mid + 1, end)
    else:
        return binary_util(input, item, begin, mid-1 )


def binary_search(input, item):
    begin = 0
    end = len(input) - 1
    
    return binary_util(input,item, begin, end)



input = [1,2,3,4,5,6,7,8,9]

assert binary_search(input, 5) == 4
assert binary_search(input, 9) == 8
assert binary_search(input, 1) == 0
assert binary_search(input, 20) == None
assert binary_search(input, -1) == None