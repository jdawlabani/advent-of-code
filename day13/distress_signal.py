import ast




def compare(left: int | list, right: int | list):
    match(left,right):
        case int(), int():
                if not left == right:
                    return right - left
                else:
                    return 0
        case list(), int():
            new_right = []
            new_right.append(right)
            return compare(left[0],new_right[0])
        case list(), list():
            short = min(len(right),len(left))
            for i in range(short):
                # print(left[i],' ',right[i])
                return compare(left[i],right[i])
        case int(), list():
            new_left = []
            new_left.append(left)
            return compare(new_left[0],right[0])

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
    arr = read_input('ex1.txt')
    for i in range (len(arr[0])):
        if compare(arr[0][i],arr[1][i]) > 0:
            in_order += 1
    print('IN ORDER:', in_order)




