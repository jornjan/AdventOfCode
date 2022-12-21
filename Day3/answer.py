with open('./Day3/input.txt', 'r') as inputFile:
    data = inputFile.read().splitlines()


score_dict = {}
for i in range(26):
    score_dict[chr(ord('a')+i)] = i+1
    score_dict[chr(ord('A')+i)] = i+1+26

### Part 1
part1_doubles = []
for line in data:
    first_half = set(line[:len(line)//2])
    second_half = set(line[len(line)//2:])

    part1_doubles.append(first_half.intersection(second_half).pop())


part1_scores = [score_dict.get(x) for x in part1_doubles]
print(f'Part 1: {sum(part1_scores)}')


### Part 2
part2_badges = []
for i in range(0, len(data), 3):
    temp_data = data[i:i+3]
    part2_badges.append(set(temp_data[0]).intersection(
                        set(temp_data[1]).intersection(
                        set(temp_data[2]))).pop())


part2_scores = [score_dict.get(x) for x in part2_badges]
print(f'Part 2: {sum(part2_scores)}')