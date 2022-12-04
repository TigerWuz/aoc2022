from utils.inputReader import InputReader

priority_dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8,
    "i" : 9,
    "j" : 10,
    "k" : 11,
    "l" : 12,
    "m" : 13,
    "n" : 14,
    "o" : 15,
    "p" : 16,
    "q" : 17,
    "r" : 18,
    "s" : 19,
    "t" : 20,
    "u" : 21,
    "v" : 22,
    "w" : 23,
    "x" : 24,
    "y" : 25,
    "z" : 26,
    "A" : 27,
    "B" : 28,
    "C" : 29,
    "D" : 30,
    "E" : 31,
    "F" : 32,
    "G" : 33,
    "H" : 34,
    "I" : 35,
    "J" : 36,
    "K" : 37,
    "L" : 38,
    "M" : 39,
    "N" : 40,
    "O" : 41,
    "P" : 42,
    "Q" : 43,
    "R" : 44,
    "S" : 45,
    "T" : 46,
    "U" : 47,
    "V" : 48,
    "W" : 49,
    "X" : 50,
    "Y" : 51,
    "Z" : 52 
}


def day3():
    input = InputReader.get("input\\day3.txt")
    priorities = []
    #split the input strings in half
    for line in input:
        first, second = line[:len(line)//2], line[len(line)//2:]

        d ={}

        for c in first:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        common = ""

        for c in second:
            if c in d and d[c] > 0:
                common += c
                d[c] -= 1

        priorities.append(priority_dict[common[0]])

        # print("Common letter is \"{}\", Priority is: {}".format(common, priority_dict[common[0]]))

    print("Part 1 Priority Sum: {}".format(sum(priorities)))

def day3_b():
    input = InputReader.get("input\\day3.txt")
    priorities = []

    for i in range(0, len(input), 3):
        d_first = {}
        d_second = {}
        d_third = {}
        first = input[i]
        second = input[i+1]
        third = input[i+2]

        for c in first:
            if c in d_first:
                d_first[c] += 1
            else:
                d_first[c] = 1

        for c in second:
            if c in d_second:
                d_second[c] += 1
            else:
                d_second[c] = 1

        for c in third:
            if c in d_third:
                d_third[c] += 1
            else:
                d_third[c] = 1

        combined_dicts = [d_first, d_second, d_third]
        common_keys = set(d_first.keys())
        for d in combined_dicts[1:]:
            common_keys.intersection_update(set(d.keys()))

        #transform set to list
        # priority_dict[list(common_keys)[0]]
        priorities.append(priority_dict[list(common_keys)[0]])

    print("Part 2 Sum of Priorities: {}".format(sum(priorities)))

day3()
day3_b()