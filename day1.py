from utils.inputReader import InputReader

class Elf():
    def __init__(self) -> None:
        self.food = []

    def get_calories_sum(self):
        return sum(self.food)
 
def day_1_a():
    input = InputReader.get("input\\day1.txt")

    elves = []
    elf = Elf()
    for i in input:
        if i is'':
            elves.append(elf)
            elf = Elf()
        else:
            elf.food.append(int(i))
    elves.append(elf)
    
    calories_per_elf = []
    for elf in elves:
        calories_per_elf.append(elf.get_calories_sum())
    
    calories_per_elf.sort(reverse=True)

    print("Solution Day 1 Part 1: {}".format(calories_per_elf[0]))
    print("Solution DAy 1 Part 2: {}".format(sum(calories_per_elf[0:3])))

day_1_a()
