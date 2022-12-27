f = open('input.txt', 'r')
g = open('ex2.txt','r')
contents = f.read().strip().split('\n')
# queue will hold two values: queue[0] will be either noop or the value to add and queue[1] will be the number of cycles left before execution
queue = []
cycle = 0
x = 1
signal = 0

for command in contents:
    c = command.split(' ')
    match c[0]:
        case 'noop':
            queue.append(['noop', 1])
        case 'addx':
            queue.append([int(c[1]), 2])
    cycle +=1
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal += (x * cycle)
    queue[0][1] -= 1
    if queue[0][1] == 0:
        p = queue.pop(0)
        if p[0] == 'noop':
            continue
        else:
            x += p[0]
    
while len(queue) > 0:
    cycle +=1
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal += (x * cycle)
    queue[0][1] -= 1
    if queue[0][1] == 0:
        p = queue.pop(0)
        if p[0] == 'noop':
            continue
        else:
            x += p[0]

# print(x)
# print(cycle)
print("---- PART 1: -----\n" +str(signal))