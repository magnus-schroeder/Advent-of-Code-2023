def solution(lines):
    extrapolated_values = []
    for line in lines:
        values = list(map(int, line.split()))
        first_values = []
        while True:
            if not any(value != 0 for value in values):
                break
            differences = []
            for i, value in enumerate(values[1:]):
                differences.append(value - values[i])
            first_values.append(values[0])
            values = differences
        first_values.reverse()
        extrapolated_value = first_values[0]
        for first_value in first_values[1:]:
            extrapolated_value = first_value - extrapolated_value
        extrapolated_values.append(extrapolated_value)
    return sum(extrapolated_values)


if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
