def solution(lines):
    points = 0
    for line in lines:
        winning_numbers, all_numbers = list(
            map(lambda el: set(filter(lambda num: num != '', el.split(' '))), line.split(': ')[1].split(' | '))
        )
        hits = len(winning_numbers.intersection(all_numbers))
        if hits >= 1:
            points += 2 ** (hits - 1)
    return points


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
