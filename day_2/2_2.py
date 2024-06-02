import re

def extract_colors(string):
    pattern = r'(\d+) red,?|(\d+) blue,?|(\d+) green,?'
    regex_pattern = re.compile(pattern)

    matches = regex_pattern.findall(string)
    color_dict = {'red': 0, 'blue': 0, 'green': 0}
    
    for match in matches:
        for idx, group in enumerate(match):
            if group:
                if idx == 0:
                    color_dict['red'] = int(group)
                elif idx == 1:
                    color_dict['blue'] = int(group)
                elif idx == 2:
                    color_dict['green'] = int(group)

    return color_dict

def main():

    game_cube_power = 0

    with open('day_2\\input.txt', 'r') as f:
        for game in f:
            
            max_red = 0
            max_blue = 0
            max_green = 0

            game = game.strip('\n')
            game = game.split(';')
            for round in game:
                cubes_shown = extract_colors(round)
                if cubes_shown['red'] >= max_red:
                    max_red = cubes_shown['red']
                if cubes_shown['blue'] >= max_blue:
                    max_blue = cubes_shown['blue']
                if cubes_shown['green'] >= max_green:
                    max_green = cubes_shown['green']

            game_cube_power += max_red * max_blue * max_green


    print(f'Sum of cube powers = {game_cube_power}')



    

if __name__ == '__main__':
    main()