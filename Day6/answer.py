import numpy as np

with open('./Day6/input.txt', 'r') as inputFile:
    data = inputFile.read()

data = [x for x in data]


def find_distinct_loc(data: list, n: int) -> int:
    for i in range(len(data)-n):
        if len(np.unique(data[i:i+n])) == n:
            return i+n


# Part 1
print(f'Part 1 answer: {find_distinct_loc(data, 4)}')

# Part 2
print(f'Part 2 answer: {find_distinct_loc(data, 14)}')