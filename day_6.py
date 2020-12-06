from functools import reduce
test_input ="""abc

a
b
c

ab
ac

a
a
a
a

b"""

test_result_1=11
test_result_2=6

def get_answer_sets(codes):
    return [list(map(set,group.split("\n"))) for group in codes.split("\n\n")]

def summed_answers_1(codes):
    return sum([len(reduce(set.union, group)) for group in get_answer_sets(codes)])

def summed_answers_2(codes):
    return sum([len(reduce(set.intersection, group)) for group in get_answer_sets(codes)])
assert summed_answers_1(test_input) == test_result_1
assert summed_answers_2(test_input) == test_result_2

with open("input_day_6.txt") as f:
    content=f.read()
    print(summed_answers_1(content))
    print(summed_answers_2(content))