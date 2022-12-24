f = open('input.txt','r')
contents = f.read().strip().split('\n')
# grid where tail has stepped
tail_coordinates = []
# x and y coordinates
head_x = 0
head_y = 0
tail_x = 0
tail_y = 0


def move(direction, steps, h_x, h_y, t_x, t_y, t_coordinates):
    match direction:
        case 'U':
            for i in range(steps):
                h_y -= 1
                if(abs(h_y - t_y) != 1):
                    t_y -= 1
                    if str(t_x)+','+str(t_y) not in t_coordinates:
                        t_coordinates.append(str(t_x)+','+str(t_y))
        case 'D':
            for i in range(steps):
                h_y += 1
                if(abs(h_y - t_y) != 1):
                    t_y += 1
                    if str(t_x)+','+str(t_y) not in t_coordinates:
                        t_coordinates.append(str(t_x)+','+str(t_y))
        case 'L':
            for i in range(steps):
                h_x -= 1
                if(abs(h_x - t_x) != 1):
                    t_x -= 1
                    if str(t_x)+','+str(t_y) not in t_coordinates:
                        t_coordinates.append(str(t_x)+','+str(t_y))
        case 'R':
            for i in range(steps):
                h_x -= 1
                if(abs(h_x - t_x) != 1):
                    t_x -= 1
                    if str(t_x)+','+str(t_y) not in t_coordinates:
                        t_coordinates.append(str(t_x)+','+str(t_y))

for command in contents:
    c = command.split(' ')
    move(c[0], int(c[1]), head_x, head_y, tail_x, tail_y, tail_coordinates)

print(len(tail_coordinates))
