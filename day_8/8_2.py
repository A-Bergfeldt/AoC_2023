from itertools import cycle
from math import lcm

with open('day_8/input.txt', 'r') as file:
    data_dict = {}
    direction_line = file.readline().strip()
    file.readline()
    for line in file:
        key, value = line.strip().split(' = ')
        value = value.strip('()').split(', ')
        data_dict[key] = value

key_list = list(data_dict.keys())
start_keys = [x for x in key_list if x.endswith('A')]
goal_keys = [x for x in key_list if x.endswith('Z')]
shortest_steps = []

for i in range(len(start_keys)):
    n_steps = 0
    current_key = start_keys[i]

    for direction in cycle(direction_line):
        if current_key in goal_keys:
            break
        n_steps += 1
        if direction == 'L':
            current_key = data_dict[current_key][0]
        elif direction == 'R':
            current_key = data_dict[current_key][1]
    shortest_steps.append(n_steps)

print(f' Shortest path = {lcm(*shortest_steps)}')