from utils.inputReader import InputReader
import re

def day4():
    input = InputReader.get("input\\day4.txt")
    elf_pairs = []


    for i in input:
        s = re.split('-|,', i)
        s = [int(x) for x in s]
        elf_pairs.append(s)
    
    overlaps = 0

    for ep in elf_pairs:
        if ep[0] <= ep[2] and ep[1] >= ep[3]:
            overlaps += 1
        elif ep[0] >= ep[2] and ep[1] <= ep[3]:
            overlaps += 1

    print("Part 1: Sum of overlapping Areas: {}".format(overlaps))

def day4_b():
    input = InputReader.get("input\\day4.txt")
    elf_pairs = []

    for i in input:
        s = re.split('-|,', i)
        s = [int(x) for x in s]
        elf_pairs.append(s)
    
    overlaps= len(input)

    # search if the two aread do not overlap at all
    for ep in elf_pairs:
        if ep[1] < ep[2]:
            overlaps -= 1
        elif ep[3] < ep[0]:
            overlaps -= 1

    print("Part 2: Sum of overlapping Areas: {}".format(overlaps))

#day4()
day4_b()