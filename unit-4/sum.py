
def sum(input):
    if len(input) == 0:
        return 0
    else:
        return input.pop(0) + sum(input[0:])
    
input = [10 , 20 , 20 , 10]

assert sum(input) ==  60