def binary_search(input, item):
    begin = 0
    end = len(input) - 1

    while begin <= end:
        mid = int((begin + end) / 2)
        if input[mid] == item:
            return mid

        if input[mid] > item:
            end = mid - 1 
        else:
            begin = mid + 1
        

    return None


input = [1,2,3,4,5,6,7,8,9]

assert binary_search(input, 5) == 4
assert binary_search(input, 9) == 8
assert binary_search(input, 1) == 0
assert binary_search(input, 20) == None