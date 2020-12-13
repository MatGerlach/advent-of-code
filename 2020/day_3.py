from functools import reduce
test_input=[
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]
test_result_1=7
test_result_2=336

def validate_1_oneline(o):
    return sum([1 if o[y][y*3 % len(o[0])] == "#" else 0 for y in range(len(o))])

def validate_2_oneline(o):
    return reduce(lambda x,y: x*y,[sum([1 if o[y][y*z[0]//z[1] % len(o[0])] == "#" else 0 for y in range(0,len(o),z[1])]) for z in [(1,1),(3,1),(5,1),(7,1),(1,2)]],1)

assert validate_1_oneline(test_input) == test_result_1
assert validate_2_oneline(test_input) == test_result_2
with open("./input_day_3.txt") as f:
    original=f.read().splitlines()

validate_2_oneline(original)