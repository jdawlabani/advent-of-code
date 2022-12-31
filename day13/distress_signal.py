f = open('input.txt', 'r')
g = open('ex1.txt', 'r')
contents = g.read().split('\n')



def compare(left: int | list, right: int | list):
    match(left,right):
        case int(), int():
            return (left - right)
        case list(), int():
            
        case list(), list():

def read_input(input):
    left = []
    right = []
    i = 0
    index = 0
    in_order = 0
    for line in input:
        if i == 0:
            left.append(line)
            i == 1
        elif i == 1:
            right.append(line)
    for i in range(len(right)):
        if compare(left[i],right[i]) > :
            in_order += 1
    return in_order











read_input(contents)


