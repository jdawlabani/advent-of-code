f = open('input.txt','r')
# g = open('ex1.txt', 'r')
grid = f.read().strip().split('\n')
width = len(grid[0])
length = len(grid)
counted_trees = []
count = 0
max_score = 0



# PART 1
for i in range(width):
    for j in range(length):
        b_score = 1
        r_score = 1
        t_score = 1
        l_score = 1
        # counts all the trees on the outside
        if (i == 0 or i==length or j == 0 or j == width):
            count += 1
        else:
            # check from top
            visible = True
            counted = False
            for k in range(i-1,-1,-1):
                if(int(grid[i][j]) <= int(grid[k][j])):
                    t_score = i - k
                    visible = False
                    # print("false top: " + str(i) + " "+str(j))
                    break
                else:
                    t_score = i
            if visible and not counted:
                counted = True
                count += 1
                # counted_trees.append("top " + str(i) + " " + str(j))

            # check from bottom
            visible = True
            for k in range(i+1,length):
                if(int(grid[i][j]) <= int(grid[k][j])):
                    visible = False
                    b_score = k - i
                    # print("false bottom: " + str(i) + " "+str(j))
                    break
                else:
                    b_score = k
            if visible and not counted:
                counted = True
                count += 1
                # counted_trees.append("bottom " +str(i) + " " + str(j))
            
            # check from left
            visible = True
            for k in range(j-1,-1,-1):
                if(int(grid[i][j]) <= int(grid[i][k])):
                    visible = False
                    l_score = j - k
                    # print("false left: " + str(i) + " "+str(j))
                    break
                else:
                    l_score = j
            if visible and not counted:
                counted = True
                count += 1
                # counted_trees.append("left " + str(i) + " " + str(j))

            # check from right
            visible = True
            for k in range(j+1,width):
                if(int(grid[i][j]) <= int(grid[i][k])):
                    visible = False
                    r_score = k - j
                    # print("false right: " + str(i) + " "+str(j))
                    break
                else:
                    r_score = k
            if visible and not counted:
                counted = True
                count += 1
                # counted_trees.append("right "+str(i) + " " + str(j))
                
            score = (l_score*t_score*b_score*r_score)
            print(str(i) + " " + str(j) + " " + str(l_score) + " " + str(r_score)+ " " + str(t_score)+ " " + str(b_score))
            if(score > max_score):
                max_score = score
                # print(score)

print(count)
print(max_score)
# print(counted_trees)

