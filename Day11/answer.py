with open('./Day11/input.txt', 'r') as f:
    data = f.read().splitlines()

data = [x.lstrip().strip(':') for x in data]
print(data)

class Item():
    def __init__(self, lvl: int) -> None:
        self.lvl = lvl
    
    def __repr__(self) -> str:
        return str(self.lvl)


class Monkey():
    def __init__(self, idx: int) -> None:
        self.number: int = idx
        self.items: list = []

        self.div: int
        self.true_target: int
        self.false_target: int 
        self.operation: str
    
    def add_item(self, item: Item):
        self.items.append(item)

    def set_div(self, div: int):
        self.div = div
    
    def set_true_target(self, target: int):
        self.true_target = target

    def set_false_target(self, target: int):
        self.false_target = target

    def set_operation(self, operation: str):
        self.operation = operation
        pass

    def __repr__(self) -> str:
        out = f"""
        Monkey: {self.number}
        Items: {self.items}
        Test: divisible by {self.div}
        If True: {self.true_target}
        If False: {self.false_target}
        Operation: {self.operation}
        """
        return out

monkeys: list = []
current_monkey:Monkey = None

for line in data:
    if line=='':
        continue

    elif line.startswith('Monkey'):
        idx = int(line.split()[1])
        current_monkey = Monkey(idx)
        monkeys.append(current_monkey)

    elif line.startswith('Starting items:'):
        items = line.split(':')[1].split(',')
        items = [int(x) for x in items]
        for x in items:
            current_monkey.add_item(Item(x))

    elif line.startswith('Test:'):
        div = int(line.split()[-1])
        current_monkey.set_div(div)

    elif line.startswith('If true'):
        target = int(line.split()[-1])
        current_monkey.set_true_target(target)

    elif line.startswith('If false'):
        target = int(line.split()[-1])
        current_monkey.set_false_target(target)
    
    elif line.startswith('Operation:'):
        current_monkey.set_operation(line.replace('Operation: new = ', ''))


eval
for m in monkeys: print(m)
