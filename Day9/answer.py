with open('./Day9/input.txt', 'r') as f:
    data = f.read().splitlines()

import numpy as np


class Knot():
    def __init__(self, pos: tuple) -> None:
        self.x: int = pos[0]
        self.y: int = pos[1]
    
    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def move_relative(self, other):
        lagx = other.x - self.x
        lagy = other.y - self.y

        if abs(lagx)>1 or abs(lagy)>1:
            self.x += np.sign(lagx)
            self.y += np.sign(lagy)

delta_dict = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}

grid_size = 1000
starting_pos = grid_size//2, grid_size//2


n_knots = 10
knots = [Knot(starting_pos) for _ in range(n_knots)]
knot1_positions = np.zeros((grid_size,grid_size), dtype=int)
knot9_positions = np.zeros((grid_size,grid_size), dtype=int)

for motion in data:
    orient, n = motion.split()
    n = int(n)
    
    for i in range(n):
        dx, dy = delta_dict[orient]

        knots[0].move(dx, dy)
        for i in range(1, len(knots)):
            knots[i].move_relative(knots[i-1])


        knot1_positions[knots[1].x, knots[1].y] = 1
        knot9_positions[knots[9].x, knots[9].y] = 1


print(f'Part 1 answer: {knot1_positions.flatten().sum()}')
print(f'Part 2 answer: {knot9_positions.flatten().sum()}')