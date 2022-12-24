f = open('input.txt','r')
g = open('ex1.txt', 'r')
grid = f.read().strip().split('\n')
width = len(grid[0])
length = len(grid)
counted_trees = []
count = 0

# PART 1
for i in range(width):
    for j in range(length):
        # counts all the trees on the outside
        if (i == 0 or i==length or j == 0 or j == width):
            count += 1
        else:
            # check from top
            visible = True
            counted = False
            for k in range(i-1,-1,-1):
                if(int(grid[i][j]) <= int(grid[k][j])):
                    visible = False
                    # print("false top: " + str(i) + " "+str(j))
                    break
            if visible and not counted:
                counted = True
                count += 1
                # counted_trees.append("top " + str(i) + " " + str(j))
            # check from bottom
            if not visible:
                visible = True
                for k in range(i+1,length):
                    if(int(grid[i][j]) <= int(grid[k][j])):
                        visible = False
                        # print("false bottom: " + str(i) + " "+str(j))
                        break
                if visible and not counted:
                    counted = True
                    count += 1
                    # counted_trees.append("bottom " +str(i) + " " + str(j))
            
            # check from left
            if not visible:
                visible = True
                for k in range(j-1,-1,-1):
                    if(int(grid[i][j]) <= int(grid[i][k])):
                        visible = False
                        # print("false left: " + str(i) + " "+str(j))
                        break
                if visible and not counted:
                    counted = True
                    count += 1
                    # counted_trees.append("left " + str(i) + " " + str(j))

            if not visible:
                visible = True
                # check from right
                for k in range(j+1,width):
                    if(int(grid[i][j]) <= int(grid[i][k])):
                        visible = False
                        # print("false right: " + str(i) + " "+str(j))
                        break
                if visible and not counted:
                    counted = True
                    count += 1
                    # counted_trees.append("right "+str(i) + " " + str(j))
print(count)
# print(counted_trees)

