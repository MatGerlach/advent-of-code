import re
test_input="""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

test_result_1=2

def validate(inputs):
    return sum([len((set(['ecl','pid','eyr','hcl','byr','iyr','hgt']) ^ set(dict(re.findall("(\S{3}):(\S+)", i, re.MULTILINE)).keys()))-set(['cid'])) == 0 for i in inputs.split("\n\n")])
with open("input_day_4.txt") as f:
    print(validate(f.read()))