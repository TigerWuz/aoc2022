from utils.inputReader import InputReader

# A X Rock 1
# B Y Paper 2
# C Z Scissors 3

def play(input):
    opponent = input[0]
    me = input[1]
    score = 0

    if opponent is 'A': 
        if me is 'X':
            score = 3 + 1 # Draw + Rock
        elif me is 'Y':
            score = 6 + 2
        else:
            score = 0 + 3
    elif opponent is 'B':
        if me is 'X':
            score = 0 + 1 # Loose + Rock
        elif me is 'Y':
            score = 3 + 2
        else:
            score = 6 + 3
    else:
        if me is 'X':
            score = 6 + 1 # Win + Rock
        elif me is 'Y':
            score = 0 + 2
        else:
            score = 3 + 3
        
    return score

# A Rock 1
# B Paper 2
# C Scissors 3

# X Loose 0
# Y Draw 3
# Z Win 6
def play_2(input):
    opponent = input[0]
    me = input[1]
    score = 0

    if opponent is 'A': 
        if me is 'X': # Loose
            score = 0 + 3 # Scissors
        elif me is 'Y': # Draw
            score = 3 + 1 # Rock
        else: # Win
            score = 6 + 2 # paper
    elif opponent is 'B':
        if me is 'X':
            score = 0 + 1 # Loose + Rock
        elif me is 'Y':
            score = 3 + 2 # Draw + Paper
        else:
            score = 6 + 3 # Win + Scissors
    else:
        if me is 'X':
            score = 0 + 2 # Loose + Paper
        elif me is 'Y': # Draw + Scissors
            score = 3 + 3
        else:
            score = 6 + 1 # Win + Rock
        
    return score
 
def day_2_a():
    input = InputReader.get("input\\day2.txt")
    score = []
    for elem in input:
        result = play(elem.split(' '))
        score.append(result)

    print("Solution 1 Total Score: {}".format(sum(score)))

    score = []
    for elem in input:
        result = play_2(elem.split(' '))
        score.append(result)

    print("Solution 2 Total Score: {}".format(sum(score)))


day_2_a()
