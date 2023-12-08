import utils
import re


def _cell_exists(matrix, line, x):
    if x < 0 or line < 0:
        return False
    return line < len(matrix) and x < len(matrix[line])


def _is_symbol(matrix, line, x):
    if _cell_exists(matrix, line, x):
        char = matrix[line][x]
        return not utils.is_digit(char) and not char == "."
    else:
        return False


def _is_digit(matrix, line, x):
    if _cell_exists(matrix, line, x):
        return utils.is_digit(matrix[line][x])
    else:
        return False


def _adjacent_to_symbols(matrix, line, x):
    """Check if the number at the line and position x is adjacent to a symbol
    >>> _adjacent_to_symbols(["....","....",".398","...."],2,2)    
    False
    """
    while x < len(matrix[line]) and utils.is_digit(matrix[line][x]):
        if _is_symbol(matrix, line-1, x-1) or\
                _is_symbol(matrix, line-1, x) or\
                _is_symbol(matrix, line-1, x+1) or\
                _is_symbol(matrix, line, x-1) or\
                _is_symbol(matrix, line, x+1) or\
                _is_symbol(matrix, line+1, x-1) or\
                _is_symbol(matrix, line+1, x) or\
                _is_symbol(matrix, line+1, x+1):
            return True
        x += 1
    return False


def _get_number(matrix, line, x):
    # find start
    while _is_digit(matrix, line, x-1):
        x -= 1
    number = ""
    while _is_digit(matrix, line, x):
        number += matrix[line][x]
        x += 1
    return int(number)


def _get_adjacent_numbers(matrix, line, x):
    """
    >>> _get_adjacent_numbers(["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."],1,3)
    [467, 35]
    """
    numbers = []
    # top
    if _is_digit(matrix, line-1, x):
        numbers.append(_get_number(matrix, line-1, x))
    else:
        if _is_digit(matrix, line-1, x-1):
            numbers.append(_get_number(matrix, line-1, x-1))
        if _is_digit(matrix, line-1, x+1):
            numbers.append(_get_number(matrix, line-1, x+1))
    # same
    if _is_digit(matrix, line, x-1):
        numbers.append(_get_number(matrix, line, x-1))
    if _is_digit(matrix, line, x+1):
        numbers.append(_get_number(matrix, line, x+1))
    # bottom
    if _is_digit(matrix, line+1, x):
        numbers.append(_get_number(matrix, line+1, x))
    else:
        if _is_digit(matrix, line+1, x-1):
            numbers.append(_get_number(matrix, line+1, x-1))
        if _is_digit(matrix, line+1, x+1):
            numbers.append(_get_number(matrix, line+1, x+1))
    return numbers


def task_1(input):
    """
    >>> task_1(["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."])
    4361
    """
    sum = 0
    for line, content in enumerate(input):
        for match in re.finditer(r"\d+", content):
            if _adjacent_to_symbols(input, line, match.start()):
                sum += int(match.group())
    return sum


def task_2(input):
    """
    >>> task_2(["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."])
    467835
    """
    sum = 0
    for line, content in enumerate(input):
        for match in re.finditer(r"\*", content):
            numbers = _get_adjacent_numbers(input, line, match.start())
            print(numbers)
            if len(numbers) == 2:
                sum += numbers[0]*numbers[1]

    return sum


if __name__ == "__main__":
    print("Solution 1:")
    input = utils.load_input(3)
    print(task_1(input))
    print("Solution 2:")
    print(task_2(input))
