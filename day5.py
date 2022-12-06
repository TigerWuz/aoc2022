from utils.inputReader import InputReader
from collections import namedtuple

NR_OF_STACKS = 9

CraneCommand = namedtuple('CraneCommand', ('amount', 'origin', 'destination'))


def day5_a():
    input = InputReader.get("input\\day5.txt")

    #Create and fìll stacks
    stacks = [ [] for _ in range(NR_OF_STACKS)]

    for line in input:
        if line.startswith('move'):
            break

        current =  [line[i:i+4] for i in range(0, len(line), 4)]

        for i, c in enumerate(current):
            if c.startswith('['):
                val = c.replace('[', '').replace(']', '').replace(' ', '')
                stacks[i].append(val)
            else:
                continue

    for s in stacks:
        s.reverse()

    #create orders
    orders = []
    for line in input:
        if line.startswith('move'):
            keywords = line.split(' ')
            cc = CraneCommand(amount = int(keywords[1]),
                        origin = int(keywords[3]),
                        destination = int(keywords[5]))
            orders.append(cc)

    #reaarange stacks
    for order in orders:
        for a in range(order.amount):
            stacks[order.destination-1].append(stacks[order.origin-1].pop())

    solution = ''
    for s in stacks:
        solution = solution + s[-1]
    print("Day 5 Solution 1: {}".format(solution))

def day5_b():
    input = InputReader.get("input\\day5.txt")

    #Create and fìll stacks
    stacks = [ [] for _ in range(NR_OF_STACKS)]

    for line in input:
        if line.startswith('move'):
            break

        current =  [line[i:i+4] for i in range(0, len(line), 4)]

        for i, c in enumerate(current):
            if c.startswith('['):
                val = c.replace('[', '').replace(']', '').replace(' ', '')
                stacks[i].append(val)
            else:
                continue

    for s in stacks:
        s.reverse()

    #create orders
    orders = []
    for line in input:
        if line.startswith('move'):
            keywords = line.split(' ')
            cc = CraneCommand(amount = int(keywords[1]),
                        origin = int(keywords[3]),
                        destination = int(keywords[5]))
            orders.append(cc)

    #reaarange stacks
    for order in orders:
        crates = stacks[order.origin-1][len(stacks[order.origin-1])-order.amount:]
        stacks[order.destination-1] = stacks[order.destination-1] + crates
        stacks[order.origin-1] = stacks[order.origin-1][:-order.amount]

    solution = ''
    for s in stacks:
        solution = solution + s[-1]
    print("Day 5 Solution 1: {}".format(solution))

day5_b()
