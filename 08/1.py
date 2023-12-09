def solution(lines):
    instructions = [*lines[0]]
    elements = {}
    for line in lines[2:]:
        elements[line[:3]] = {'L': line[7:10], 'R': line[12:15]}
    i = 0
    position = 'AAA'
    while True:
        if position == 'ZZZ':
            break
        position = elements[position][instructions[i % len(instructions)]]
        i += 1
    return i


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
