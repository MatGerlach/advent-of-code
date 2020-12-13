test_input_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
test_input_2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
                45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]


def step_1(adapters):
    sorted_input = sorted(map(int, adapters))
    diffs = list(
        map(lambda x, y: int(x)-int(y), sorted_input[1:], sorted_input[:-1]))
    assert max(diffs) <= 3
    assert min(diffs) >= 1
    return (diffs.count(1)+1)*(diffs.count(3)+1)


def prev_step(number, valid, already_known):
    # already_known is a reference to a shared object
    # A little bit hacky
    if number in already_known:  # No need to calculate again
        return already_known[number]
    elif number == 0:  # Reached the bottom
        return 1
    elif number > 0 and number in valid:  # Let's compute all possible way to this number
        possible_ways = prev_step(
            number-1, valid, already_known) + prev_step(number-2, valid, already_known) + prev_step(number-3, valid, already_known)
        already_known[number] = possible_ways
        return possible_ways
    else:  # Not positive or not in the adapters
        return 0


def step_2(adapters):
    sorted_adapters = sorted(map(int, adapters))
    device_input = max(sorted_adapters) + 3
    sorted_adapters = [0] + sorted_adapters + [device_input]
    return prev_step(device_input, sorted_adapters, {})


assert step_1(test_input_1) == 35
assert step_2(test_input_1) == 8
assert step_1(test_input_2) == 220
assert step_2(test_input_2) == 19208

with open("input_day_10.txt") as f:
    challenge_input = f.read().splitlines()
print(step_1(challenge_input))
print(step_2(challenge_input))
