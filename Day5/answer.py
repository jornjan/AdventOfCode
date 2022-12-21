with open('./Day5/input.txt', 'r') as inputFile:
    data = inputFile.read().splitlines()


start_state = data[:8]
start_state.reverse()
moves = data[10:]

## Part 1
state_dict = {i:[] for i in range(1, 10)}
for line in start_state:
    for i, idx in enumerate(range(1, len(line), 4)):
        state_dict[i+1] += [line[idx]] if line[idx]!= ' ' else []


for move in moves:
    move = move.split(' ')
    n = int(move[1])
    src = int(move[3])
    dest = int(move[5])

    for i in range(n):
        state_dict[dest].append(state_dict[src].pop())

part1_ans = ''.join(state_dict[i][-1] for i in state_dict)
print(f'Part 1: {part1_ans}')



## Part 2
state_dict = {i:[] for i in range(1, 10)}
for line in start_state:
    for i, idx in enumerate(range(1, len(line), 4)):
        state_dict[i+1] += [line[idx]] if line[idx]!= ' ' else []


for move in moves:
    move = move.split(' ')
    n = int(move[1])
    src = int(move[3])
    dest = int(move[5])

    state_dict[dest].extend(state_dict[src][-n:])
    state_dict[src] = state_dict[src][:-n]


part2_ans = ''.join(state_dict[i][-1] for i in state_dict)
print(f'Part 2: {part2_ans}')