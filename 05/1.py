import math


def solution(lines):
    seeds = list(map(int, lines[0][7:].split()))
    almanac = [[], [], [], [], [], [], []]
    lowest_location = math.inf
    i = -2
    for line in lines[1:]:
        if line == '' or line.endswith(':'):
            i += 1
        else:
            almanac[i // 2].append(list(map(int, line.split())))
    for seed in seeds:
        destination = seed
        for destination_maps in almanac:
            for destination_map in destination_maps:
                if destination in range(destination_map[1], destination_map[1] + destination_map[2]):
                    destination += destination_map[0] - destination_map[1]
                    break
        if destination < lowest_location:
            lowest_location = destination
    return lowest_location


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
