import copy


f = open('input.txt', 'r')
g = open('ex1.txt', 'r')
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

def load(contents,monkeys):
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
                num = items[i][0:2]
                monkeys[-1].items.append(int(num))
            # print(monkeys[-1].items)
            # print(items)
        if "Operation:" in command[0]:
            op = command[0].split(' ')
            monkeys[-1].operation.append(op[-2])
            monkeys[-1].operation.append(op[-1])
            # print(monkeys[-1].operation)
        if "Test:" in command[0]:
            t = command[0].split(' ')
            monkeys[-1].test = int(t[-1])
            # print(monkeys[-1].test)
        if "If true:" in command[0]:
            t = command[0].split(' ')
            monkeys[-1].to_monkey.append(int(t[-1]))
        if "If false:" in command[0]:
            f = command[0].split(' ')
            monkeys[-1].to_monkey.append(int(f[-1]))

def rounds(num_of_rounds,monkeys, relief):
    # combined all the mods from tests together and mod results by this if no relief(divide by 3)
    combined_mod = 1
    for m in monkeys:
        combined_mod = combined_mod * m.test
    for i in range(num_of_rounds):
        for m in monkeys:
            for j in range(len(m.items)):
                m.inspected += 1
                if m.operation[0] == '+':
                    if m.operation[1] == 'old':
                        m.items[0] = m.items[0] * 2
                    else:
                        m.items[0] = m.items[0] + int(m.operation[1])
                elif m.operation[0] == '-':
                    if m.operation[1] == 'old':
                        m.items[0] = m.items[0] - m.items[0]
                    else:
                        m.items[0] = m.items[0] - int(m.operation[1])
                elif m.operation[0] == '*':
                    if m.operation[1] == 'old':
                        m.items[0] = m.items[0] * m.items[0]
                    else:
                        m.items[0] = m.items[0] * int(m.operation[1])
                else:
                    if m.operation[1] == 'old':
                        m.items[0] = m.items[0] / m.items[0]
                    else:
                        m.items[0] = m.items[0] / int(m.operation[1])
                if (relief):
                    m.items[0] = m.items[0] // 3

                # move the item to the monkey it belongs to 
                send = m.items.pop(0)
                if send % m.test == 0:
                    monkeys[m.to_monkey[0]].items.append(send)
                else:
                    send = send % combined_mod
                    monkeys[m.to_monkey[1]].items.append(send)
    top2 = [0,0]
    for m in monkeys:
        if m.inspected > top2[0] and m.inspected > top2[1] and top2[0] <= top2[1]:
            top2[0] = m.inspected
        elif m.inspected > top2[1]:
            top2[1] = m.inspected
    return top2[0] * top2[1]







load(contents, monkeys)
monkeys2 = copy.deepcopy(monkeys)
print("---PART 1:---\n" +str(rounds(20,monkeys, True)))
print("---PART 2:---\n" +str(rounds(10000,monkeys2,False)))


    



