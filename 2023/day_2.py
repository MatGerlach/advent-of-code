import utils
import re


def _max_count(color, line):
    """Get the maximum count of a color in a given line
    >>> _max_count("blue","Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    6
    """
    counts = re.findall(r"(\d+) " + color, line)
    return max(map(int, counts))


def task_1(input):
    """
    >>> task_1(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green","Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue","Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"])
    8
    """
    sum = 0
    for line in input:
        game_number = int(re.search(r"Game (\d+):.*", line).group(1))
        if _max_count("blue", line) > 14 or\
                _max_count("green", line) > 13 or\
                _max_count("red", line) > 12:
            continue
        sum += game_number
    return sum


def task_2(input):
    """
    >>> task_2(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green","Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue","Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"])
    2286
    """
    sum = 0
    for line in input:
        sum += _max_count("blue", line) *\
            _max_count("red", line) *\
            _max_count("green", line)
    return sum


if __name__ == "__main__":
    print("Solution 1:")
    input = utils.load_input(2)
    print(task_1(input))
    print("Solution 2:")
    print(task_2(input))
