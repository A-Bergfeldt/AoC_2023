import re

def get_number(line, x_start_coord):
    number = ''
    sliced_line = line[x_start_coord:] + '.'
    for i in range(len(sliced_line)):
        if sliced_line[i].isdigit():
            number += sliced_line[i]
        else:
            break
    return number

def is_adjacent(start_coord, num, symbol_dict):
    num_len = len(num)
    x1 = start_coord[0] - 1
    y1 = start_coord[1] - 1
    x2 = start_coord[0] + num_len
    y2 = start_coord[1] + 1

    for symbol in symbol_dict:
        x = symbol[0]
        y = symbol[1]
        if x1 <= x <= x2 and y1 <= y <= y2:
            if symbol_dict[symbol] == -1:
                symbol_dict[symbol] = [num]
            else:
                symbol_dict[symbol].append(num)
    return symbol_dict

def main():
    symbol_dict = {}
    numbers = []
    number_start_coord = []

    with open('day_3\\input.txt', 'r') as f:
        y_coord = 0
        for line in f:
            line = line.strip('\n')
            y_coord += 1
            for x_coord in range(len(line)):
                if re.match(r'\*', line[x_coord]): # get gear cooridnate
                    symbol_dict[(x_coord, y_coord)] = -1

                elif x_coord == 0 and line[x_coord].isdigit(): # get number value and coordinate
                    numbers.append(get_number(line, x_coord))
                    number_start_coord.append((x_coord, y_coord))
                elif not line[x_coord-1].isdigit() and line[x_coord].isdigit():
                    numbers.append(get_number(line, x_coord))
                    number_start_coord.append((x_coord, y_coord))

    gear_ratio = 0
    
    for i in range(len(numbers)):
        symbol_dict = is_adjacent(number_start_coord[i], numbers[i], symbol_dict)

    print(symbol_dict)
    for key in symbol_dict:
        if len(symbol_dict[key]) == 2:
            gear_ratio += int(symbol_dict[key][0]) * int(symbol_dict[key][1])

    print(f'Gear ratio is: {gear_ratio}')

if __name__ == '__main__':
    main()