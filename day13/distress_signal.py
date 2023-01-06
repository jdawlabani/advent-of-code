import ast
from functools import cmp_to_key




def compare(left: int | list, right: int | list) -> int:
    match left, right:
        case int(), int():
            return (left < right) - (left > right)
        case list(), list():
            for cmp_val in map(compare, left, right):
                if cmp_val:
                    return cmp_val
            return compare(len(left), len(right))
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])

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
    in_order = 0
    arr = read_input('input.txt')
    for i in range (len(arr[0])):
        if compare(arr[0][i],arr[1][i]) > 0:
            in_order += 1
    print('IN ORDER:', in_order)




