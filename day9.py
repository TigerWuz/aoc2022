from utils.inputReader import InputReader
from utils.point import Point as P_Point

class Point(P_Point):
    def move_towards(self, point):
        dx, dy = self.manhattan_distance(point)

        if abs(dx) >= 2:
            if dx > 0 :
                self.x += 1
            else:
                self.x -= 1

            if abs(dy) == 1:
                self.y += dy

        if abs(dy) >= 2:
            if dy > 0 :
                self.y += 1
            else:
                self.y -= 1

            if abs(dx) == 1:
                self.x += dx

def day9_a():
    input = InputReader.get('input\\day9.txt')

    head = Point(0, 0)
    tail = Point(0, 0)
    visited = {(0, 0)}

    for command in input:
        direction, distance = command.split()
        distance = range(int(distance))

        for _ in distance:
            head.move(direction)
            tail.move_towards(head)
            visited.add(tail.getPos())
            
    solution = len(visited)
    print("Solution Day 9 Part 1: Visited Points {}".format(solution))

def day9_b():
    input = InputReader.get('input\\day9.txt')

    rope = [Point(0, 0) for _ in range(10)]
    visited = {(0, 0)}

    for command in input:
        direction, distance = command.split()
        distance = range(int(distance))

        for _ in distance:
            rope[0].move(direction)

            for i in range(1, len(rope)):
                rope[i].move_towards(rope[i-1])

            visited.add(rope[9].getPos())

    solution = len(visited)
    print("Solution Day 9 Part 2: Visited Points {}".format(solution))

# day9_a()
day9_b()
