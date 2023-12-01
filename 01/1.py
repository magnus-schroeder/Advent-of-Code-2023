import re


def solution(lines):
    return map(lambda line: int(line[0] + line[-1]),
               map(lambda line: re.sub("[^0-9]", "", line), lines)
               )


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(sum(solution([line.rstrip() for line in input_file])))
