def max(input):
    if len(input) == 0:
        return 0
    else:
        n1 = input[0]
        maxNumber = (max(input[1:]))
        if n1 > maxNumber:
            return n1
        else:
            return maxNumber

input = [9,2, 1, 5 , 2]
assert max(input) == 9