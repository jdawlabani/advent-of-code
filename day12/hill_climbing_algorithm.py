f = open('input.txt', 'r')
g = open('ex1.txt', 'r')
# put SE in the front so you will always go to it
alphabet = 'SEabcdefghijklmnopqrstuvwxyz'
contents = g.readlines()
grid = []
for line in contents:
    l = line.split('\n')
    grid.append(l[0])

def find_start(grid):
    for y in range(len(grid)):
        try:
            x = grid[y].index('S')
            return [x,y]
        except:
            continue

# c is coordinates of where you are now, we will keep track of path
def find_path(c, grid, path):
    if grid[c[1]][c[0]] == 'E':
        return path
    # up
    if (not c[1] == 0) and alphabet.index(grid[c[1]][c[0]]) - alphabet.index(grid[c[1]][c[0] - 1]) <= 1:
        print('up') 
    # down
    # left
    # right

c = [1,2]
find_path(find_start(grid),grid,'')




