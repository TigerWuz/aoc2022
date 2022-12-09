class Point:
    directions = {
        'U' : ( 1,  0),
        'D' : (-1,  0),
        'L' : ( 0, -1),
        'R' : ( 0,  1)
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Direction can be on of the upper letters
    def move(self, direction):
        self.x += self.directions[direction][0]
        self.y += self.directions[direction][1]

    def manhattan_distance(self, point):
        return point.x - self.x,  point.y - self.y

    def getPos(self):
        return self.x, self.y
