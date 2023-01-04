f = open('input.txt', 'r')
g = open('ex1.txt', 'r')
contents = g.read().split('\n')



def compare(left: int | list, right: int | list):
    match(left,right):
        case int(), int():
            return 1
        case list(), int():
            return 2
        case list(), list():
            return 3
        case int(), list():
            return 4
def read_input(input):
    left = []
    right = []
    direction = 0
    index = 0
    in_order = 0
    for line in input:
        if direction == 0:
            left.append(line)
            direction = 1
        elif direction == 1:
            right.append(line)
            direction = 0
    print("-----LEFT-----")
    for i in range(len(left)):
        print(left[i])
    print("-----RIGHT-----")
    for i in range(len(right)):
        print(right[i])
    # for i in range(len(right)):
    #     if compare(left[i],right[i]) >= 1:
    #         in_order += 1
    # return in_order











print(read_input(contents))



