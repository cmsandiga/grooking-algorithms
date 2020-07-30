
def find_min_index(elements):
    min_e = elements[0]
    min_i = 0
    for i in range(len(elements)):
        if elements[i] < min_e:
            min_e = elements[i]
            min_i = i
    return min_i 

def selection_sort(elements):
    result = []

    for i in range(len(elements)) :
        min_index = find_min_index(elements)
        result.append(examples.pop(min_index))
    return result

examples = [1 ,9 , 4, 3 , 2]


print(selection_sort(examples))