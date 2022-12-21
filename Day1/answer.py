with open('./Day1/input.txt', 'r') as inputFile:
    data = inputFile.readlines()

output = []
temp_list = []
for line in data:
    if line.startswith('\n'):
        output.append(sum(temp_list))
        temp_list.clear()
    else:
        temp_list.append(int(line[:-1]))

output = sorted(output, reverse=True)

print(f'Ex 1:\nThe elve carrying the most calories carries: {output[0]}\n')
print(f'Ex 2:\nThe top 3 carrying elves carry a total of: {sum(output[:3])}\n')