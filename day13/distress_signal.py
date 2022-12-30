f = open('input.txt', 'r')
g = open('ex1.txt', 'r')
contents = g.read().split('\n')

left = []
right = []
def read_input(input):
    i = 0
    for line in input:
        if i == 0:
            left.append(line)
            i += 1
        elif i == 1:
            right.append(line)
            i += 1
        else:
            i = 0
    print(left)
    print(right)

def compare(left, right):
    