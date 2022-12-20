import re

f = open('input.txt', 'r')
contents = f.readlines()
part_1_count = 0
part_2_count = 0
for line in contents:
    # split line into array of the numbers and assign cast them into ints, then check if one range is contained in another
    split = re.split(r'[-,\n]', line)
    left_start = int(split[0])
    left_end = int(split[1])
    right_start = int(split[2])
    right_end = int(split[3])
    # part 1 check (one range is completely within the other range)
    if((left_start <= right_start and left_end >= right_end) or (left_start >= right_start and left_end <= right_end)):
        part_1_count += 1
    #part 2 check (ANY overlap between the two ranges)
    if((left_start >= right_start and left_start <= right_end) or (left_end >= right_start and left_end <= right_end) or (right_start >= left_start and right_start <= left_end) or (right_end >= left_start and right_end <= left_end)):
        part_2_count += 1
print("PART 1 answer: " + str(part_1_count))
print("PART 2 answer: " + str(part_2_count))
f.close()
