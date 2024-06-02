import re

def main():
    text_to_int_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
    }

    total = 0

    with open('day_1\\input.txt', 'r') as f:
        for line in f:
            for key in text_to_int_dict:
                line = line.replace(key, f'{key}{text_to_int_dict[key]}{key}') # 'key' 'int' 'key' as to not break "eightwo"
            vals = (re.sub('\D', '', line))
            cal_val = int(f'{vals[0]}{vals[-1]}')
            total += cal_val
    print(f'Calibration value sum = {total}')


if __name__ == '__main__':
    main()