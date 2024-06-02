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
    game_idx = 0
    game_idx_sum = 0
    with open('day_2\\input.txt', 'r') as f:
        for game in f:
            game_idx += 1
            game_possible = True
            game = game.strip('\n')
            game = game.split(';')
            for round in game:
                cubes_shown = extract_colors(round)
                if cubes_shown['red'] >= 13:
                    game_possible = False
                elif cubes_shown['blue'] >= 15:
                    game_possible = False
                elif cubes_shown['green'] >= 14:
                    game_possible = False
            if  game_possible:
                game_idx_sum += game_idx

    print(f'Sum of indexes for possible games = {game_idx_sum}')



    

if __name__ == '__main__':
    main()