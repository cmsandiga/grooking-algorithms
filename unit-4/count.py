
def count_numbers(input):
    if len(input) == 0:
        return 0
    else:
        return 1 + count_numbers(input[1:])
    
input = [10 , 20 , 30 , 10]

assert count_numbers(input) == 4