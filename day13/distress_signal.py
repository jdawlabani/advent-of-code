import ast




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
def read_input(input: str) -> list:
    left = []
    right = []
    # determines where to store the input of the line 0 =>left, 1=> right, -1=> blank line
    direction = 0
    index = 0
    in_order = 0
    f = open(input, 'r')
    contents = f.read().split('\n')
    for line in contents:
        if direction == 0:
            left.append(ast.literal_eval(line))
            direction = 1
        elif direction == 1:
            right.append(ast.literal_eval(line))
            direction = -1
        else:
            direction = 0
    return [left, right]

if __name__ == "__main__":
    print('---PART 1:---')
    arr = read_input('input.txt')
    compare(arr[0],arr[1])



