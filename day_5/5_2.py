import re
import numpy as np

def x_to_y(input, destination_ranges, source_ranges, ranges_list):
    for i in range(len(source_ranges)):
        if  source_ranges[i] <= input <= source_ranges[i] + ranges_list[i]-1:
            return input - (source_ranges[i] - destination_ranges[i])
    return input

def parse_data(data):
    maps = re.split(r'\n\n', data.strip())
    parsed_data = {}

    seeds_line = maps[0]
    seeds_key, seeds_values = re.match('(.+):\s*(.+)', seeds_line).groups()
    parsed_data[seeds_key] = [int(x) for x in seeds_values.split()]
    
    for section in maps[1:]:
        lines = section.split('\n')
        key = lines[0]
        values = [(map(int, re.split('\s+', line))) for line in lines[1:]]
        columns = list(map(list, zip(*values))) 
        parsed_data[key] = columns
    
    return parsed_data

with open('day_5/input.txt', 'r') as file:
    parsed_data = parse_data(file.read())
    lowest_loc = np.inf
    for i in range(0, len(parsed_data['seeds']), 2):
        for j in range(parsed_data['seeds'][i+1] + 1):
            seed = parsed_data['seeds'][i] + j 
            input = seed
            for key, maps in parsed_data.items():
                if key != 'seeds':
                    input = x_to_y(input, maps[0], maps[1], maps[2])
            if input < lowest_loc:
                lowest_loc = input

print(f'Lowest location for any seed = {lowest_loc}')


