import math


def solution(lines):
    time, distance = int(lines[0][11:].replace(' ', '')), int(lines[1][11:].replace(' ', ''))
    return (math.ceil((time / 2) + math.sqrt((time / 2) ** 2 - distance))
            - math.floor((time / 2) - math.sqrt((time / 2) ** 2 - distance)) - 1)


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
