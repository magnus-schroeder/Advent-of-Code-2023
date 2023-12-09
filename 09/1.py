def solution(lines):
    extrapolated_values = []
    for line in lines:
        values = list(map(int, line.split()))
        last_values = []
        while True:
            if not any(value != 0 for value in values):
                break
            differences = []
            for i, value in enumerate(values[1:]):
                differences.append(value - values[i])
            last_values.append(values[-1])
            values = differences
        extrapolated_values.append(sum(last_values))
    return sum(extrapolated_values)


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
