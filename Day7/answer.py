with open('./Day7/input.txt', 'r') as inputFile:
    data = inputFile.read().splitlines()


class Directory():
    def __init__(self, name: str, parent) -> None:
        self.name = name
        self.parent = parent

        self.childs: dict = {}
        self.files: list = []
        self.size=None

    def add_dir(self, name: str):
        self.childs[name] = self.__class__(name, self)
        return self.childs[name]
    
    def add_file(self, name: str):
        self.files.append(name)
    
    def get_size(self):
        if self.size is None:
            self.compute_size()
        return self.size

    def compute_size(self):
        total = 0
        for c in self.childs:
            total += self.childs[c].get_size()

        for f in self.files:
            total += int(f.split(' ')[0])

        self.size = total
    
    def print_contents(self, offset):
        print(' '*offset + '-' + self.name + ' ' + str(self.get_size()))

        for f in self.files:
            fsize, fname = f.split(' ')
            print(' '*(offset+10) + '-' + fname + ' ' + str(fsize))
        
        for c in self.childs:
            self.childs[c].print_contents(offset+2)

root = Directory('/', None)
all_dirs = [root]

current_dir = root
for line in data:
    # Skip first
    if line.startswith('$ cd /'):
        print('hi')
        continue

    # commands
    if line.startswith('$ cd'):
        target_dir = line.split(' ')[-1]
        if target_dir == '..':
            current_dir = current_dir.parent
        else:
            current_dir = current_dir.childs[target_dir]
    
    elif line.startswith('$ ls'):
        continue
    
    elif line.startswith('dir'):
        dirname = line.split(' ')[1]
        all_dirs.append(current_dir.add_dir(dirname))
    else:
        current_dir.add_file(line)

total = 0
for d in all_dirs:
    temp_size = d.get_size()
    if temp_size<=100000:
        total += temp_size

print(f'Part 1 answer: {total}')


req_size = 30000000 - (70000000 - root.get_size())
sizes = []
for d in all_dirs:
    temp_size = d.get_size()
    if temp_size >= req_size:
        sizes.append(temp_size)
        

print(f'Part 2 answer: {min(sizes)}')