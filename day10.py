from utils.inputReader import InputReader

def day10():
    input = InputReader.get('input\\day10.txt')

    cmd_stack = []
    cycle = 0
    register_x = 1
    solution = []
    crt = []

    for line in input:
        if line == 'noop':
            cmd_stack.append(0)
        elif line.startswith('addx'):
            _, value = line.split(' ')
            cmd_stack.append(0)
            cmd_stack.append(int(value))

    while len(cmd_stack) > 0:
        if (cycle % 40) == 0:
            crt.append('\n')
        
        d_pixel = abs((cycle % 40) - register_x)
        if d_pixel <= 1:
            crt.append(u'\u2588')   #Draws a box which is nicer to read
        else:
            crt.append(' ')

        cycle += 1
        register_x += cmd_stack.pop(0)

        if (cycle % 40) == 19:
            print('Cycle {} Register X: {}, Signal Strength {}'.format(cycle, register_x, (cycle+1) * register_x))
            solution.append((cycle+1) * register_x)

    print('Solution Day 10 A: {}'.format(sum(solution)))
    print('Solution Day 10 B:')
    print(''.join(crt))

day10()
