def load_input(day):
    with open(f"input_day_{day}.txt") as f:
        return f.read().splitlines()


def is_digit(symbol):
    return symbol in "0123456789"
