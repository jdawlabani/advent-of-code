import re
f = open('input.txt','r')
class Directory:
    def __init__(self, parent, name, children):
        self.parent = parent
        self.name = name,
        self.children = {}

current_dir = ''

for i in f:
    # split the command into an array
    command = re.split(r'[ \n]', i)
    # pop off the last command which will be an empty string because of \n
    command.pop()

    match command[0]:
        case '$':
            match command[1]:
                case 'cd':
                    match command[2]:
                        case '..':

                        case _:


                    


