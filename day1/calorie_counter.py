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


