from utils.inputReader import InputReader

def day6_a():
    input = InputReader.get("input\\day6.txt")
    
    sequence = []
    startOfSequence = 0

    for i, letter in enumerate(input[0]):
        sequence.append(letter)
        
        setCheck = set(sequence)
        if len(setCheck) == 4:
            startOfSequence = i+1
            break
        elif len(sequence) >= 4:
            sequence = sequence[1:]


    solution = startOfSequence
    print("Solution A: First four different letters start at: {}".format(solution))

def day6_b():
    input = InputReader.get("input\\day6.txt")
    
    sequence = []
    startOfSequence = 0

    for i, letter in enumerate(input[0]):
        sequence.append(letter)
        
        setCheck = set(sequence)
        if len(setCheck) == 14:
            startOfSequence = i+1
            break
        elif len(sequence) >= 14:
            sequence = sequence[1:]


    solution = startOfSequence
    print("Solution B: First 14 different letters start at: {}".format(solution))

# day6_a()
day6_b()
