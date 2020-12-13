test_input="""939
7,13,x,x,59,x,31,19"""


def get_result_1(text):
    earliest_starttime=int(text.splitlines()[0])
    busnumbers=[int(x) for x in text.splitlines(1)[1].split(",") if x != "x"]
    earliest_depart=sorted(map(lambda x: (x,(earliest_starttime//x + 1)*x),busnumbers),key=lambda x:x[1])
    return earliest_depart[0][0]*(earliest_depart[0][1]-earliest_starttime)
assert get_result_1(test_input) == 295

with open("input_day_13.txt") as f:
    text=f.read()
print(get_result_1(text))

# Chinese remainder is what we are searching for step 2
# To lazy to implement myself:
# From https://rosettacode.org/wiki/Chinese_remainder_theorem#Functional
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def get_result_2(text):
    enumeration = dict(enumerate(text.splitlines()[-1].split(",")))
    enumeration = dict(filter(lambda x: x[1] != "x",enumeration.items()))
    mods = list(map(int,enumeration.values()))
    remainders = list(map(lambda x,y: x-y, mods,enumeration.keys()))
    return chinese_remainder(mods, remainders)

assert get_result_2(test_input) == 1068781
assert get_result_2("17,x,13,19") == 3417
assert get_result_2("67,7,59,61") == 754018
assert get_result_2("67,x,7,59,61") == 779210
assert get_result_2("67,7,x,59,61") == 1261476
assert get_result_2("1789,37,47,1889") == 1202161486
print(get_result_2(text))