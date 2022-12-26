f = open('input.txt', 'r')
contents = f.read().strip().split('\n')
queue = []
cycle = 0
x = 0
signal = 0

for command in contents:
    c = command.split(' ')
    match c[0]:
        case 'noop':
            queue.append(['noop', 1])
        case 'addx':
            queue.append([int(c[1]), 2])
    cycle +=1
    queue[0][1] -= 1
    if queue[0][1] == 0:
        p = queue.pop(0)
        print(p)
    if type(p[0]) == 'int':
        x += p[0]
print(x)
