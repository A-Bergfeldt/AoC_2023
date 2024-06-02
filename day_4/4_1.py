import re

def main():
    with open('day_4\\input.txt', 'r') as f:

        total_points = 0

        for line in f:
            n_wins = 0
            line = re.split('\:|\|', line)
            win_nrs = re.findall('\d+', line[1])
            nrs = re.findall('\d+',line[2])

            for nr in nrs:
                if nr in win_nrs:
                    n_wins += 1

            if n_wins:
                total_points += 2**(n_wins - 1)
    
    print(f'Total scratchcard point = {total_points}')

                    
if __name__ == '__main__':
    main()