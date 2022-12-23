import re
f = open('input.txt','r')
class Directory:
    def __init__(self, parent, path, children):
        self.parent = parent
        self.path = path
        self.children = {}
        self.files = {}
        # keep the size of the directory that way for deletion we only have to go as deep as the limit
        self.size = 0


current_dir = Directory(None, 'root',{})
# add the root to the directory
current_dir.children.update({'/': Directory(current_dir,'/',{})})
root_dir = current_dir.children['/']
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
                            current_dir = current_dir.parent
                        case _:
                            current_dir = current_dir.children[command[2]]
                case 'ls':
                    pass
        case 'dir':
            current_dir.children.update({command[1]: Directory(current_dir, current_dir.path+ '/' +command[1], {})})
            print(current_dir.path)
        case _:
            current_dir.files.update({command[1]:command[0]})
            # update the size of both the current directory and its parent directories
            current_dir.size += int(command[0])
            p = current_dir.parent
            while p.parent != None:
                p.size += int(command[0])
                p = p.parent


