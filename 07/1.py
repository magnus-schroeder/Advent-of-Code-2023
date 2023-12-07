def get_score(line):
    cards_score = ''
    highscore = 0
    for card in line[0]:
        cards_score += hex(card_values.index(card))[2:]
        highscore += line[0].count(card)
    return hex(highscore // 2)[2:] + cards_score


def solution(lines):
    total_winnings = 0
    for i, (_, bid) in enumerate(sorted(list(map(lambda line: (line[:5], int(line[6:])), lines)), key=get_score)):
        total_winnings += (i + 1) * bid
    return total_winnings


card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
