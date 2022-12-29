f = open('input.txt', 'r')
g = open('ex1.txt', 'r')
# put SE in the front so you will always go to it
alphabet = 'SEabcdefghijklmnopqrstuvwxyz'
contents = g.readlines()
grid = []
visited = []
for line in contents:
    l = line.split('\n')
    grid.append(l[0])

def find_start(grid):
    for y in range(len(grid)):
        try:
            x = grid[y].index('S')
            return [y,x]
        except:
            continue

# c is coordinates of where you are now, we will keep track of path
def find_path(c, grid, path,visited):
    if grid[c[0]][c[1]] == 'E':
        return path
    # up
    if (not c[0] == 0) and alphabet.index(grid[c[0]][c[1]]) - alphabet.index(grid[c[0]-1][c[1]]) <= 1 and (str(c[0]-1) + " " + str(c[1])) not in visited:
        visited.append(str(c[0]-1) + " " + str(c[1]))
        find_path([c[0]-1,c[1]], grid, path + '^',visited)
    # down
    if (not c[0] == len(grid)-2) and alphabet.index(grid[c[0]][c[1]]) - alphabet.index(grid[c[0] + 1][c[1]]) <= 1 and (str(c[0]+1) + " " + str(c[1])) not in visited:
        visited.append(str(c[0]+1) + " " + str(c[1]))
        find_path([c[0] + 1,c[1]], grid, path + 'v',visited)
    # left
    if (not c[1] == 0) and alphabet.index(grid[c[0]][c[1]]) - alphabet.index(grid[c[0]][c[1]-1]) <= 1 and (str(c[0]) + " " + str(c[1] - 1)) not in visited:
        visited.append(str(c[0]) + " " + str(c[1] - 1))
        find_path([c[0],c[1]-1], grid, path + '<',visited)
    # right
    if (not c[1] == len(grid[0]-2)) and alphabet.index(grid[c[0]][c[1]]) - alphabet.index(grid[c[0]][c[1]+1]) <= 1 and (str(c[0]) + " " + str(c[1] + 1)) not in visited:
        visited.append(str(c[0]) + " " + str(c[1] + 1))
        find_path([c[0],c[1]+1], grid, path + '>',visited)


start = find_start(grid)
find_path(start,grid,'',[str(start[0]) + " " + str(start[1])])




