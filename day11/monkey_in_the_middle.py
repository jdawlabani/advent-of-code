f = open('input.txt', 'r')
contents = f.readlines()


class Monkey:
    def __init__(self, id, items, inspected, operation, test, to_monkey):
        self.id = id
        # worry level of the items each monkey has
        self.items = items
        # number of items inspected
        self.inspected = inspected
        # operation[0] is operator, operation[1] is either number or "old"
        self.operation = operation
        # will be a single number, since all tests are divisible by number
        self.test = test
        # to_monkey[0] if true, to_monkey[1] if flase
        self.to_monkey = to_monkey

monkeys = []
count = 0

for line in contents:
    command = line.strip().split('\n')
    # print(command)
    if "Monkey" in command[0]:
        id = command[0].split(' ')
        id = id[1][0]
        monkeys.append(Monkey(id,[],0,[],None,[]))
    if "Starting items:" in command[0]:
        items = command[0].split(' ')
        for i in range(2,len(items)):
            num = items[i]
            
        print(monkeys[-1].items)
        print(items)
    if "Operation:" in command[0]:
        print("operation")
    if "Test:" in command[0]:
        print("test")
    if "If true:" in command[0]:
        print("true")
    if "If false:" in command[0]:
        print("false")


    



