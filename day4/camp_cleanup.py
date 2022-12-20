import re
# PART 1
f = open('input.txt', 'r')
contents = f.readlines()
count = 0
for line in contents:
    # split line into array of the numbers and assign cast them into ints, then check if one range is contained in another
    split = re.split(r'[-,\n]', line)
    left_start = int(split[0])
    left_end = int(split[1])
    right_start = int(split[2])
    right_end = int(split[3])
    if((left_start <= right_start and left_end >= right_end) or (left_start >= right_start and left_end <= right_end)):
        count += 1
        print(split)
print(count)

