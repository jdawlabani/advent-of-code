f = open('input.txt', 'r')
g = open('ex1.txt', 'r')
contents = g.read().split('\n')
print(contents)

for line in contents:
    print()