import math


def solution(lines):
    record_product = 1
    distances = list(map(int, lines[1][11:].split()))
    for i, time in enumerate(list(map(int, lines[0][11:].split()))):
        record_product *= (math.ceil((time / 2) + math.sqrt((time / 2) ** 2 - distances[i]))
                           - math.floor((time / 2) - math.sqrt((time / 2) ** 2 - distances[i])) - 1)
    return record_product


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
