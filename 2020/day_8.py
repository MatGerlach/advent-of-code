from copy import deepcopy


def parse_line(line):
    if "nop" in line:
        return (1, 0, line)
    elif "acc" in line:
        return (1, int(line.split(" ")[1]), line)
    elif "jmp" in line:
        return (int(line.split(" ")[1]), 0, line)


def parse_input(text):
    if "\n" in text:
        text = text.splitlines()
    lines = [parse_line(l)for l in text]
    return lines


def run_lines(lines):
    pointer_history = []
    pointer = 0
    acc = 0
    while pointer not in pointer_history and pointer < len(lines):
        pointer_history.append(pointer)
        acc += lines[pointer][1]
        pointer += lines[pointer][0]
    return (acc, pointer_history)


def brute_force_change(lines):
    changeset = run_lines(lines)[1]
    changeset = set(filter(lambda i: lines[i][1] == 0, changeset))
    for line_nr in changeset:
        line = lines[line_nr][2]
        new_lines = deepcopy(lines)
        if "jmp" in line:
            new_lines[line_nr] = (1, 0, line)
        elif "nop" in lines[line_nr][2]:
            new_lines[line_nr] = (int(line.split(" ")[1]), 0, line)
        (new_acc, new_changeset) = run_lines(new_lines)
        if len(lines)-1 in new_changeset:
            return new_acc


with open("input_day_8.txt") as f:
    lines = parse_input(f.read())
print("Step 1: The accumulator stopped at {}".format(run_lines(lines)[0]))
print("Step 2: The accumulator stopped at {}".format(brute_force_change(lines)))


def test_run_lines():
    text = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    assert run_lines(parse_input(text))[0] == 5


def test_brute_force_change():
    text = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    assert brute_force_change(parse_input(text)) == 8
