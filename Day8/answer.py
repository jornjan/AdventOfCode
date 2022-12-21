with open('./Day8/input.txt', 'r') as inputFile:
    data = inputFile.read().splitlines()

import numpy as np
import itertools

data = np.asarray([[int(x) for x in y] for y in data])


class Tree(object):
    def __init__(self, x: int, y: int, height: int) -> None:
        self.x = x
        self.y = y
        self.height = height
    
    def add_neighbours(self, treegrid: np.ndarray) -> None:
        self.left  = None if self.x==0  else treegrid[self.x-1, self.y]
        self.right = None if self.x==98 else treegrid[self.x+1, self.y]
        self.top   = None if self.y==0  else treegrid[self.x, self.y-1]
        self.bot   = None if self.y==98 else treegrid[self.x, self.y+1]

    def left_smaller(self, other) -> bool:
        if other==self or other.height>self.height:
            return True if self.left is None else self.left.left_smaller(other)
        else:
            return False

    def right_smaller(self, other) -> bool:
        if other==self or other.height>self.height:
            return True if self.right is None else self.right.right_smaller(other)
        else:
            return False
    
    def top_smaller(self, other) -> bool:
        if other==self or other.height>self.height:
            return True if self.top is None else self.top.top_smaller(other)
        else:
            return False
    
    def bot_smaller(self, other) -> bool:
        if other==self or other.height>self.height:
            return True if self.bot is None else self.bot.bot_smaller(other)
        else:
            return False

    def visible(self) -> int:
        return int(any([self.left_smaller(self),
                        self.right_smaller(self),
                        self.top_smaller(self),
                        self.bot_smaller(self)]))
    
    def left_score(self, other, cnt=0) -> int:
        if other==self or other.height>self.height:
            return cnt if self.left is None else self.left.left_score(other, cnt=cnt+1)
        else:
            return cnt

    def right_score(self, other, cnt=0) -> int:
        if other==self or other.height>self.height:
            return cnt if self.right is None else self.right.right_score(other, cnt=cnt+1)
        else:
            return cnt

    def top_score(self, other, cnt=0) -> int:
        if other==self or other.height>self.height:
            return cnt if self.top is None else self.top.top_score(other, cnt=cnt+1)
        else:
            return cnt

    def bot_score(self, other, cnt=0) -> int:
        if other==self or other.height>self.height:
            return cnt if self.bot is None else self.bot.bot_score(other, cnt=cnt+1)
        else:
            return cnt+1

    def scenic_score(self) -> int:
        return self.left_score(self) * self.right_score(self) * self.top_score(self) * self.bot_score(self)

    def __repr__(self) -> str:
        return f'({self.x},{self.y})={self.height}'

treegrid = np.empty_like(data, dtype=Tree)
for x, y in itertools.product(range(0, data.shape[0]), range(0, data.shape[1])):
    treegrid[x,y] = Tree(x, y, data[x, y])

for x, y in itertools.product(range(0, data.shape[0]), range(0, data.shape[1])):
    treegrid[x, y].add_neighbours(treegrid)


# Part 1
visgrid = np.ones_like(data)
for x, y in itertools.product(range(1, data.shape[0]-1), range(1, data.shape[1]-1)):
    visgrid[x,y] = treegrid[x,y].visible()

print(f'Part 1 answer: {visgrid.flatten().sum()}')


# Part 2
scoregrid = np.ones_like(data)
for x, y in itertools.product(range(1, data.shape[0]-1), range(1, data.shape[1]-1)):
    scoregrid[x,y] = treegrid[x,y].scenic_score()


print(f'Part 1 answer: {scoregrid.flatten().max()}')