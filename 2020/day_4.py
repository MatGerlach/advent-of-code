import re,copy
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

def validate_1(inputs):
    return sum([len((set(['ecl','pid','eyr','hcl','byr','iyr','hgt']) ^ set(dict(re.findall("(\S{3}):(\S+)", i, re.MULTILINE)).keys()))-set(['cid'])) == 0 for i in inputs.split("\n\n")])

def validate_2(inputs):
    splitted_input = inputs.split("\n\n")

    parsed_input = map(lambda x:dict(re.findall("(\S{3}):(\S+)", x, re.MULTILINE)), splitted_input)
    valid = filter(lambda x: len(set(['ecl','pid','eyr','hcl','byr','iyr','hgt']) ^ set(x.keys())-set(['cid'])) == 0, parsed_input)
    valid = filter(lambda x: re.match("^\d{4}$",x['byr']) is not None and int(x['byr']) >= 1920 and int(x['byr']) <= 2002, valid)
    valid = filter(lambda x: re.match("^\d{4}$",x['iyr']) is not None and int(x['iyr']) >= 2010 and int(x['iyr']) <= 2020, valid)
    valid = filter(lambda x: re.match("^\d{4}$",x['eyr']) is not None and int(x['eyr']) >= 2020 and int(x['eyr']) <= 2030, valid)
    valid = filter(lambda x: ((re.match("^\d{2}\s*in$",x['hgt']) is not None and int(x['hgt'][:2]) >= 59 and int(x['hgt'][:2]) <= 76) or
                              (re.match("^\d{3}\s*cm$",x['hgt']) is not None and int(x['hgt'][:3]) >= 150 and int(x['hgt'][:3]) <= 193)), valid)
    valid = filter(lambda x: re.match("^#[0-9a-f]{6}$",x['hcl']) is not None, valid)
    valid = filter(lambda x: re.match("^amb|blu|brn|gry|grn|hzl|oth$",x['ecl']) is not None, valid)
    valid = filter(lambda x: re.match("^\d{9}$",x['pid']) is not None, valid)
    
    return list(valid)

with open("input_day_4.txt") as f:
    print(len(validate_2(f.read())))