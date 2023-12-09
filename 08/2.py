import math


def solution(lines):
    instructions = [*lines[0]]
    elements = {}
    for line in lines[2:]:
        elements[line[:3]] = {'L': line[7:10], 'R': line[12:15]}
    counts = []
    for start_position in list(filter(lambda key: key.endswith('A'), elements.keys())):
        position = start_position
        i = 0
        while True:
            if position.endswith('Z'):
                counts.append(i)
                break
            position = elements[position][instructions[i % len(instructions)]]
            i += 1
    return math.lcm(*counts)


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
