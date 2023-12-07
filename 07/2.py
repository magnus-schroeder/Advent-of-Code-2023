def get_score(line):
    cards_score = ''
    score_sum = 0
    highscore = 0
    jokers = 0
    for card in line[0]:
        cards_score += hex(card_values.index(card))[2:]
        if card == 'J':
            jokers += 1
        else:
            score = line[0].count(card)
            score_sum += score
            if score > highscore:
                highscore = score
    return hex((score_sum + jokers * (2 * highscore + jokers)) // 2)[2:] + cards_score


def solution(lines):
    total_winnings = 0
    for i, (_, bid) in enumerate(sorted(list(map(lambda line: (line[:5], int(line[6:])), lines)), key=get_score)):
        total_winnings += (i + 1) * bid
    return total_winnings


card_values = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

if __name__ == '__main__':
    with open('i.txt') as input_file:
        print(solution([line.rstrip() for line in input_file]))
