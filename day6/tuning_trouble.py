# link to problem: https://adventofcode.com/2022/day/6
# How many characters need to be processed before the first start-of-message marker is detected?

f = open('input.txt', 'r')
# the input is only one line
contents = f.readline()

def find_marker(contents, size):
    for i in range(0,len(contents)-size):
        is_marker = True
        marker = contents[i:i+size]
        sorted_marker = ''.join(sorted(marker))
        for j in range(size-1):
            if sorted_marker[j] == sorted_marker[j+1]:
                is_marker = False
        # to the end of the marker so add 4 to i(the start of the marker)
        if is_marker:
            print(i+size)
            break

# PART 1:
find_marker(contents, 4)

# PART 2:
find_marker(contents, 14)
