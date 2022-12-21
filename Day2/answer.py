with open('./Day2/input.txt', 'r') as inputFile:
    data = inputFile.read().splitlines()

score_dict_part1 = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

part1_scores = [score_dict_part1.get(x) for x in data]
print(f'Part 1: {sum(part1_scores)}')

##### Part 2 #####
score_dict_part2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}

part2_scores = [score_dict_part2.get(x) for x in data]
print(f'Part 2: {sum(part2_scores)}')