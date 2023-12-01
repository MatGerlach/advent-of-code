import utils
import re

def _parse_digit(digit):
    """Takes either a digit character or the digit name and returns the digit character
    >>> _parse_digit("1")
    '1'
    >>> _parse_digit("six")
    '6'
    """
    DIGITS = {"one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"}
    if(len(digit)>1):
        digit=DIGITS[digit]
    return digit


def _calibrate(input, regex_first, regex_last):
    calibration_value = 0
    for line in input:
        first = str(re.search(regex_first, line).group(1))
        last = str(re.search(regex_last, line).group(1))
        number = int(_parse_digit(first)+_parse_digit(last))
        calibration_value += number
    return calibration_value


def calibrate_1(input):
    """
    >>> calibrate_1(["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"])
    142
    """
    return _calibrate(input, r"^.*?(\d)", r"^.*(\d)")


def calibrate_2(input):
    """
    >>> calibrate_2(["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"])
    281
    """
    return _calibrate(input, 
                      r"^.*?(\d|one|two|three|four|five|six|seven|eight|nine)", 
                      r"^.*(\d|one|two|three|four|five|six|seven|eight|nine)")

if __name__ == "__main__":
    print("Solution 1:")
    input = utils.load_input(1)
    print(calibrate_1(input))
    print("Solution 2:")
    print(calibrate_2(input))
