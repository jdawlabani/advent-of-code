
# PART 1: finds the elf with the most calories
# open the file and place all the lines into contents
f = open('input.txt', 'r')
contents = f.readlines()
max_cal = 0
sum = 0
for line in contents:
    # check if it's a blank line
    if line == "\n":
        if sum > max_cal:
            max_cal = sum
            sum = 0
        else:
            sum = 0
    else:
        # cut off the '\n' from the line and convert it to an int
        sum += int(line[:-1])
print(max_cal)
f.close()


#PART 2: finds the top 3 elves
f = open('input.txt', 'r')
contents = f.readlines()
max_cal = [0, 0, 0]
sum = 0
for line in contents:
    # check if it's a blank line
    if line == "\n":
        if sum > max_cal[0]:
            max_cal[0] = sum
            sum = 0
            # sort the array so we will only have to check the first index
            max_cal.sort()
        else:
            sum = 0
    else:
        # cut off the '\n' from the line and convert it to an int
        sum += int(line[:-1])
print(max_cal[0]+max_cal[1]+max_cal[2])
f.close()


