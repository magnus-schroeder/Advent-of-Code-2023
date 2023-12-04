import math
import re


def solution(lines):
    game_id_sum = 0
    for i, line in enumerate(lines):
        color_max = {'red': 0, 'green': 0, 'blue': 0}
        for cube in re.split('[,;]', line.split(':')[1]):
            count, color = cube[1:].split(' ')
            if color_max[color] < int(count):
                color_max[color] = int(count)
        game_id_sum += math.prod(color_max.values())
    return game_id_sum


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
