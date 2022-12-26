f = open('input.txt', 'r')
g = open
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
    if cycle == 20 or 60 or 100 or 140 or 180 or 220:
        signal += (x * cycle)
    queue[0][1] -= 1
    if queue[0][1] == 0:
        p = queue.pop(0)
        print(p)
        if p[0] == 'noop':
            continue
        else:
            x += p[0]
while len(queue) == 0:
    cycle +=1
    if cycle == 20 or 60 or 100 or 140 or 180 or 220:
        signal += (x * cycle)
    queue[0][1] -= 1
    if queue[0][1] == 0:
        p = queue.pop(0)
        print(p)
        if p[0] == 'noop':
            continue
        else:
            x += p[0]

print(x)
print(cycle)