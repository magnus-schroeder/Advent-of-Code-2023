def solution(lines):
    counts = [1] * len(lines)
    for i, line in enumerate(lines):
        winning_numbers, all_numbers = list(
            map(lambda el: set(filter(lambda num: num != '', el.split(' '))), line.split(': ')[1].split(' | '))
        )
        for j in range(i + 1, i + len(winning_numbers.intersection(all_numbers)) + 1):
            counts[j] += counts[i]
    return sum(counts)


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
