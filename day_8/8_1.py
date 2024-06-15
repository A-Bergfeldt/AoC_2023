from itertools import cycle

with open('day_8/input.txt', 'r') as file:
    data_dict = {}
    direction_line = file.readline().strip()
    file.readline()
    for line in file:
        key, value = line.strip().split(' = ')
        value = value.strip('()').split(', ')
        data_dict[key] = value

key_list = list(data_dict.keys())
current_key = 'AAA'
goal_key = 'ZZZ'

n_steps = 0

for direction in cycle(direction_line):
    if current_key == goal_key:
        break
    n_steps += 1
    if direction == 'L':
        current_key = data_dict[current_key][0]
    elif direction == 'R':
        current_key = data_dict[current_key][1]

print(f'Found goal in {n_steps}')