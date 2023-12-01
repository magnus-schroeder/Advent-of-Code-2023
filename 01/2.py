def solution(line):
    first_num, last_num = None, None

    for i, el in enumerate(line):
        for key, value in number_dict.items():
            if key in line[:i]:
                first_num = value
                break
        else:
            if el.isnumeric():
                first_num = el
                break
            continue
        break

    for j, el in reversed(list(enumerate(line))):
        for key, value in number_dict.items():
            if key in line[j:]:
                last_num = value
                break
        else:
            if el.isnumeric():
                last_num = el
                break
            continue
        break

    return int(first_num + last_num)


number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(sum(map(lambda line: solution(line), [line.rstrip() for line in input_file])))
