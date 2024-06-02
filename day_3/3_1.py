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

def is_adjacent(start_coord, len, symbol_list):
    x1 = start_coord[0] - 1
    y1 = start_coord[1] - 1
    x2 = start_coord[0] + len
    y2 = start_coord[1] + 1

    for symbol in symbol_list:
        x = symbol[0]
        y = symbol[1]
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
    return False

def main():
    symbol_coords = []
    numbers = []
    number_start_coord = []

    with open('day_3\\input.txt', 'r') as f:
        y_coord = 0
        for line in f:
            line = line.strip('\n')
            y_coord += 1
            for x_coord in range(len(line)):
                if not re.match(r'[0-9.]', line[x_coord]): # get symbol cooridnate
                    symbol_coords.append((x_coord, y_coord))

                elif x_coord == 0 and line[x_coord].isdigit(): # get number value and coordinate
                    numbers.append(get_number(line, x_coord))
                    number_start_coord.append((x_coord, y_coord))
                elif not line[x_coord-1].isdigit() and line[x_coord].isdigit():
                    numbers.append(get_number(line, x_coord))
                    number_start_coord.append((x_coord, y_coord))

    #print(symbol_coords, numbers, number_start_coord)
    num_has_neighbour = []
    print(numbers)
    
    for i in range(len(numbers)):
        num_has_neighbour.append(is_adjacent(number_start_coord[i], len(numbers[i]), symbol_coords))
    print(sum(i[0] * i[1] for i in zip([int(j) for j in numbers], num_has_neighbour)))

if __name__ == '__main__':
    main()