f = open('input.txt','r')
grid = f.read().strip().split('\n')
# keep track of the counted trees so nothing gets double counted
counted_trees = []
width = len(grid[0])
length = len(grid)
visible = 0

for i in range(width):
    for j in range(length):
        # counts all the trees on the outside
        if (i == 0 or i==width or j == 0 or j == length):
            visible += 1
            counted_trees.append(str(i) + ',' + str(j))
        else:
            

