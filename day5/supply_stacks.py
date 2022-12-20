# there are 9 stacks so make an array within an array
stacks = [[],[],[],[],[],[],[],[],[]]

f = open('input.txt', 'r')
i = 0
def load_stacks(f, stacks):
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
        for crate in arr[i]:
            print(crate)

load_stacks(f, stacks)







