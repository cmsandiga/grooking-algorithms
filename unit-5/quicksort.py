


def quicksort(input):
    if len(input) <= 1:
        return input
    
    pivot = input[0]
    left  = [i for i in input[1:] if i <= pivot]
    right = [i for i in input[1:] if i > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


input = [6, 5 , 8, 1 , 2 , 3 ,7, 4, 9 , 10] 

assert quicksort(input) == list(range(1,11))
