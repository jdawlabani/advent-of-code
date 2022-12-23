f = open('input.txt','r')
grid = f.read().strip().split('\n')
# keep track of the counted trees so nothing gets double counted
counted_trees = []
width = len(grid[0])
length = len(grid)

for i in range(width):
    for j in range(length):
        
