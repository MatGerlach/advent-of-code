test_input = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95,
              102, 117, 150, 182, 127, 219, 299, 277, 309, 576]


def step_1(numbers, preamblelength):
    for x in range(preamblelength, len(numbers)):
        found = False
        for y in range(x-preamblelength, x):
            if (numbers[x] - numbers[y]) in numbers[x-preamblelength:x]:
                found = True
                break
        if not found:
            return numbers[x]


def step_2(numbers, target):
    for x in range(0, numbers.index(target)):
        y = x+1
        sublist = numbers[x:y]
        while sum(sublist) < target:
            y += 1
            sublist = numbers[x:y]
        if sum(sublist) == target:
            return min(sublist) + max(sublist)


with open("input_day_9.txt") as f:
    numbers = list(map(int, f.read().splitlines()))
assert step_1(test_input, 5) == 127
assert step_2(test_input, 127) == 62
target = step_1(numbers, 25)
print(step_2(numbers, target))
