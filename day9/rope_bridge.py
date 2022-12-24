f = open('input.txt','r')
g = open('ex2.txt', 'r')
contents = g.read().strip().split('\n')
# grid where tail has stepped, including start point
tail_coordinates = ['0,0']
# head_x, head_y, tail_x, tail_y coordinates
coordinates = [0,0,0,0]
# part 2 tail_coordinates and coordinates of all the knots
tail_coordinates_2 = ['0,0']
coordinates_2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(len(coordinates_2))


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

def move_2(direction, steps, coordinates, t_coordinates):
    match direction:
        case 'U':
            for i in range(steps):
                coordinates[1] -= 1
                for j in range(1,len(coordinates)-1,2):
                    if(abs(coordinates[j]- coordinates[j+2]) == 2):
                        coordinates[j+1] = coordinates[j-1]
                        coordinates[j+2] -= 1
                    if(abs(coordinates[j-1] - coordinates[j+1]) == 2):
                        if str(coordinates[18])+','+str(coordinates[19]) not in t_coordinates:
                            t_coordinates.append(str(coordinates[18])+','+str(coordinates[19]))
        case 'D':
            for i in range(steps):
                coordinates[1] += 1
                for j in range(1,len(coordinates)-1,2):
                    if(abs(coordinates[j] - coordinates[j+2]) == 2):
                        coordinates[j+1] = coordinates[j-1]
                        coordinates[j+2] += 1
                        if str(coordinates[18])+','+str(coordinates[19]) not in t_coordinates:
                            t_coordinates.append(str(coordinates[18])+','+str(coordinates[19]))
        case 'L':
            for i in range(steps):
                coordinates[0] -= 1
                for j in range(0,len(coordinates)-2,2):
                    if(abs(coordinates[j] - coordinates[j+2]) == 2):
                        coordinates[j+3] = coordinates[j+1]
                        coordinates[j+2] -= 1
                        if str(coordinates[18])+','+str(coordinates[19]) not in t_coordinates:
                            t_coordinates.append(str(coordinates[18])+','+str(coordinates[19]))
        case 'R':
            for i in range(steps):
                coordinates[0] += 1
                for j in range(0,len(coordinates)-2,2):
                    if(abs(coordinates[j] - coordinates[j+2]) == 2):
                        coordinates[j+3] = coordinates[j+1]
                        coordinates[j+2] += 1
                        if str(coordinates[18])+','+str(coordinates[19]) not in t_coordinates:
                            t_coordinates.append(str(coordinates[18])+','+str(coordinates[19]))
    return coordinates


for command in contents:
    c = command.split(' ')
    coordinates = move(c[0], int(c[1]), coordinates, tail_coordinates)

for command in contents:
    c = command.split(' ')
    coordinates = move_2(c[0], int(c[1]), coordinates_2, tail_coordinates_2)
    print(coordinates_2)

print("PART 1: " + str(len(tail_coordinates)))
print("PART 2: " + str(len(tail_coordinates_2)))
print(tail_coordinates_2)



