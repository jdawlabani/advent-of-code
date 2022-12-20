import re
import copy
# there are 9 stacks so make an array within an array
stacks = [[],[],[],[],[],[],[],[],[]]

f = open('input.txt', 'r')
# i = 0

def load_stacks(f, s):
    arr = []
    for i in range(10):
        line = f.readline()
        # split the line in array and only get the letter(if there is any) 
        split = [line[i+1:i+2] for i in range(0, len(line), 4)]
        arr.append(split)
    # pop the last two lines because they are a blank line and the line containing the numbers which we do not need
    arr.pop()
    arr.pop()
    for i in range(len(arr)-1, -1, -1):
        for j in range(9):
            if not arr[i][j] == ' ':
                s[j].append(arr[i][j])
    return s

stacks = load_stacks(f, stacks)
# need to deepcopy the original stack for part 2
part_2_stacks = copy.deepcopy(stacks)
# instructions are the rest of the 
instructions = f.readlines()

def part_1(instructions,stacks):
    for i in instructions:
        # splits instruction by spaces and cast numbers to variables
        split = re.split(r'[ \n]', i)
        num = int(split[1])
        from_stack = int(split[3])-1
        to_stack = int(split[5])-1
        for move in range(num):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)
    s = ''
    for stack in stacks:
        s += stack.pop()
    print(s)

def part_2(instructions, stacks):
    for i in instructions:
        # splits instruction by spaces and cast numbers to variables
        split = re.split(r'[ \n]', i)
        num = int(split[1])
        from_stack = int(split[3])-1
        to_stack = int(split[5])-1
        temp = []
        for move in range(num):
            temp.append(stacks[from_stack].pop())
        for move in range(num):
            stacks[to_stack].append(temp.pop())
    s = ''
    for stack in stacks:
        s += stack.pop()
    print(s)

part_1(instructions, stacks)
part_2(instructions, part_2_stacks)












