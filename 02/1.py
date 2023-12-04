import re


def solution(lines):
    game_id_sum = 0
    for i, line in enumerate(lines):
        color_max = {'red': 0, 'green': 0, 'blue': 0}
        for cube in re.split('[,;]', line.split(':')[1]):
            count, color = cube[1:].split(' ')
            if color_max[color] < int(count):
                color_max[color] = int(count)
            if color_max['red'] > 12 or color_max['green'] > 13 or color_max['blue'] > 14:
                break
        else:
            game_id_sum += i + 1
    return game_id_sum


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
