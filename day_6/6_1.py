import re
from numpy import roots
from math import ceil, floor, prod

def quad_solver(xx, x, c):
    sols = roots([xx, x, c])
    x_1 = int(ceil(min(sols)))
    x_2 = int(floor(max(sols)))

    return x_1, x_2

def main():

    res_list = []
    with open('day_6\\input.txt', 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = re.split('\s+', lines[i].strip('\n'))
        for i in range(len(lines[0]) -1):
            min_hold, max_hold = quad_solver(-1, int(lines[0][i+1]), -int(lines[1][i+1]))
            n_sols = (max_hold - min_hold) + 1
            res_list.append(n_sols)


    print(f'Product of ways to win = {prod(res_list)}')


if __name__ == '__main__':
    main()