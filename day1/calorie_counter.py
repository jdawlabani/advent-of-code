
f = open('input.txt', 'r')
contents = f.readlines()
max_cal = 0
sum = 0
for line in contents:
    if line == "\n":
        if sum > max_cal:
            max_cal = sum
            sum = 0
        else:
            sum = 0
    else:
        sum += int(line[:-1])
print(max_cal)


