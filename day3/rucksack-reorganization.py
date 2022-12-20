import math

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1: finding common item in two halves of a word
f = open('input.txt','r')
contents = f.readlines()
priority_sum = 0
for line in contents:
    halfway_point = math.ceil(len(line)/2 - 1)
    half_1 = line[:halfway_point]
    half_2 = line[halfway_point:-1]
    common_item = list(set(half_1)&set(half_2))
    for item in common_item:
        try:
            priority_sum += (lowercase.index(item) + 1)
        except:
            pass
        try:
            priority_sum += (uppercase.index(item) + 27)
        except:
            pass
print(priority_sum)
f.close()

# PART 2: finding common item in three word groups
def find_common_item(group,sum):
    common_item = list(set(group[0])&set(group[1])&set(group[2]))
    for item in common_item:
            try:
                sum += (lowercase.index(item) + 1)
            except:
                pass
            try:
                sum += (uppercase.index(item) + 27)
            except:
                pass
    return sum

f = open('input.txt', 'r')
contents = f.readlines()
priority_sum = 0
group = ["","",""]
count = 0
for line in contents:
    if count <= 2:
        group[count] = line[:-1]
        count += 1
    else:
        count = 1
        priority_sum = find_common_item(group, priority_sum)
        group[0] = line[:-1]
# run one last time for last group
priority_sum = find_common_item(group, priority_sum)
print(priority_sum)

