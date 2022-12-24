f = open('input.txt','r')
g = open('ex1.txt', 'r')
contents = f.read().strip().split('\n')
# grid where tail has stepped, including start point
tail_coordinates = ['0,0']
# head_x, head_y, tail_x, tail_y coordinates
coordinates = [0,0,0,0]


def move(direction, steps, coordinates, t_coordinates):
    match direction:
        case 'U':
            for i in range(steps):
                coordinates[1] -= 1
                if(abs(coordinates[1]- coordinates[3]) == 2):
                    coordinates[2] = coordinates[0]
                    coordinates[3] -= 1
                    if str(coordinates[2])+','+str(coordinates[3]) not in t_coordinates:
                        t_coordinates.append(str(coordinates[2])+','+str(coordinates[3]))
        case 'D':
            for i in range(steps):
                coordinates[1] += 1
                if(abs(coordinates[1] - coordinates[3]) == 2):
                    coordinates[2] = coordinates[0]
                    coordinates[3] += 1
                    if str(coordinates[2])+','+str(coordinates[3]) not in t_coordinates:
                        t_coordinates.append(str(coordinates[2])+','+str(coordinates[3]))
        case 'L':
            for i in range(steps):
                coordinates[0] -= 1
                if(abs(coordinates[0] - coordinates[2]) == 2):
                    coordinates[3] = coordinates[1]
                    coordinates[2] -= 1
                    if str(coordinates[2])+','+str(coordinates[3]) not in t_coordinates:
                        t_coordinates.append(str(coordinates[2])+','+str(coordinates[3]))
        case 'R':
            for i in range(steps):
                coordinates[0] += 1
                if(abs(coordinates[0] - coordinates[2]) == 2):
                    coordinates[3] = coordinates[1]
                    coordinates[2] += 1
                    if str(coordinates[2])+','+str(coordinates[3]) not in t_coordinates:
                        t_coordinates.append(str(coordinates[2])+','+str(coordinates[3]))
    return coordinates
for command in contents:
    c = command.split(' ')
    coordinates = move(c[0], int(c[1]), coordinates, tail_coordinates)


print("PART 1: " + str(len(tail_coordinates)))



