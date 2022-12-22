with open('./Day10/input.txt', 'r') as f:
    data = f.read().splitlines()


class Task():
    def __init__(self, cmd: str) -> None:
        if cmd == 'noop':
            self.timer = 1
            self.val = 0
        else:
            self.val = int(cmd.split()[1])
            self.timer = 2

    def proceed(self):
        self.timer -= 1

    def is_done(self):
        return self.timer ==0

    def execute(self, x: int):
        return x + self.val

current_task: Task = None
cycle_states: list = []
xval: int = 1

for cmd in data:
    current_task = Task(cmd)

    while not current_task.is_done():
        cycle_states.append(xval)
        current_task.proceed()
    
    xval = current_task.execute(xval)

total = 0
for i in range(20, 221, 40):
    print(f'{i} * {cycle_states[i-1]} = {i*cycle_states[i-1]}')
    total += i*cycle_states[i-1]


for i in range(0, len(cycle_states)):
    offset = i % 40
    if offset==0:
        print()
    
    current_state = cycle_states[i]
    if offset-1<=current_state<=offset+1:
        print('#', end='')
    else:
        print('.', end='')
print()
