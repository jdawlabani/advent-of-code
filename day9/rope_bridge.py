f = open('input.txt','r')
contents = f.read().strip().split('\n')
# grid where tail has stepped
tail_coordinates = []
# x and y coordinates
head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

for command in contents:
    c = command.split(' ')
    move(c[0], c[1], head_x, head_y, tail_x, tail_y, tail_coordinates)


def move(direction, steps, h_x, h_y, t_x, t_y, t_coordinates):
    match direction:
        case 'U'