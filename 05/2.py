import math


def solution(lines):
    seeds = list(map(int, lines[0][7:].split()))
    seed_ranges = []
    lowest_location = math.inf
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    almanac = [[], [], [], [], [], [], []]
    j = -2
    for line in lines[1:]:
        if line == '' or line.endswith(':'):
            j += 1
        else:
            almanac[j // 2].append(list(map(int, line.split())))
    for destination_maps in almanac:
        updated_seed_ranges = []
        for seed_range in seed_ranges:
            for destination_map in destination_maps:
                min_destination, max_destination = destination_map[1], destination_map[1] + destination_map[2]
                diff_destination = destination_map[0] - destination_map[1]
                min_seed, max_seed = seed_range
                if min_destination <= min_seed and max_seed <= max_destination:
                    updated_seed_ranges.append((min_seed + diff_destination, max_seed + diff_destination))
                    break
                elif min_seed <= min_destination and max_destination <= max_seed:
                    updated_seed_ranges.append((min_seed, min_destination))
                    updated_seed_ranges.append((max_destination, max_seed))
                    updated_seed_ranges.append((min_destination + diff_destination, max_destination + diff_destination))
                    break
                elif min_destination <= min_seed <= max_destination:
                    updated_seed_ranges.append((max_destination, max_seed))
                    updated_seed_ranges.append((min_seed + diff_destination, max_destination + diff_destination))
                    break
                elif min_destination <= max_seed <= max_destination:
                    updated_seed_ranges.append((min_seed, min_destination))
                    updated_seed_ranges.append((min_destination + diff_destination, max_seed + diff_destination))
                    break
            else:
                updated_seed_ranges.append(seed_range)
        seed_ranges = updated_seed_ranges
    for seed_range in seed_ranges:
        # check for zero because of unknown bug
        if seed_range[0] < lowest_location and seed_range[0] != 0:
            lowest_location = seed_range[0]
    return lowest_location


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
