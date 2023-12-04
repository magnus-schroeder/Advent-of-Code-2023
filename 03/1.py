import re


def solution(lines):
    part_sum = 0
    for row, line in enumerate(lines):
        part_str = ''
        for col, el in enumerate(line):
            if el.isnumeric():
                part_str += el
            if (not el.isnumeric() and part_str) or (el.isnumeric() and col == len(line) - 1):
                for i in range(row - 1, row + 2):
                    for j in range(col - len(part_str) - 1, col + 1):
                        if i in range(len(lines)) and j in range(len(line)):
                            if re.match('[^\d.]', lines[i][j]):
                                part_sum += int(part_str)
                                break
                    else:
                        continue
                    break
                part_str = ''
    return part_sum


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
