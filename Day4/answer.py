with open('./Day4/input.txt', 'r') as inputFile:
    data = inputFile.read().splitlines()


### Part 1
count = 0
for line in data:
    e1, e2 = line.split(',')

    e1_min, e1_max = (int(x) for x in e1.split('-'))
    e2_min, e2_max = (int(x) for x in e2.split('-'))

    if e1_min>=e2_min and e1_max<=e2_max:
        count+=1
    elif e2_min>=e1_min and e2_max<=e1_max:
        count+=1

print(f'Part 1 answer: {count}')


### Part 2
count = 0
for line in data:
    e1, e2 = line.split(',')

    e1_min, e1_max = (int(x) for x in e1.split('-'))
    e2_min, e2_max = (int(x) for x in e2.split('-'))

    if e1_min>=e2_min and e1_max<=e2_max:
        count+=1
    elif e2_min>=e1_min and e2_max<=e1_max:
        count+=1
    elif e1_max>=e2_min and e1_min<=e2_max:
        count+=1

print(f'Part 2 answer: {count}')       