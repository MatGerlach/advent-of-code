import utils
import re


def task_1(input):
    """
    >>> task_1(["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53" ,"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19" ,"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1" ,"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83" ,"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36" ,"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"])
    13
    """
    sum = 0
    for line in input:
        match = re.match(r"^Card\s+\d+: (.*) \| (.*)$", line)
        winners = set(match.group(1).split())
        picks = set(match.group(2).split())
        hits = len(picks.intersection(winners))
        if hits > 0:
            sum += 2 ** (hits - 1)
    return sum


def task_2(input):
    """
    >>> task_2(["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53" ,"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19" ,"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1" ,"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83" ,"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36" ,"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"])
    30
    """
    sum = 0
    # initial cardsgo
    cards = dict.fromkeys(range(1, len(input)+1), 1)
    for (index, line) in enumerate(input):
        card_number = index+1
        card_amount = cards[card_number]
        sum += card_amount
        match = re.match(r"^Card\s+\d+: (.*) \| (.*)$", line)
        winners = set(match.group(1).split())
        picks = set(match.group(2).split())
        hits = len(picks.intersection(winners))
        for i in range(card_number+1, card_number + hits+1):
            cards[i] += card_amount
    return sum


if __name__ == "__main__":
    input = utils.load_input(4)
    print("Solution 1:")
    print(task_1(input))
    print("Solution 2:")
    print(task_2(input))
