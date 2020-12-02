import re

policy_password_list=["1-3 a: abcde",
             "1-3 b: cdefg",
             "2-9 c: ccccccccc"]

REGEX_MAGIC="^(\d+)-(\d+) (\S): (\S+)$"

def validate_1(policy_password):
    m = re.fullmatch(REGEX_MAGIC,policy_password.strip())
    if m is None:
        print(policy_password)
    minimum = int(m.group(1))
    maximum = int(m.group(2))
    policy_char = m.group(3)
    password = m.group(4)
    count = password.count(policy_char)
    if count >= minimum and count <= maximum:
        return True
    else:
        return False

def validate_2(policy_password):
    m = re.fullmatch(REGEX_MAGIC,policy_password.strip())
    if m is None:
        print(policy_password)
    pos1 = int(m.group(1))-1
    pos2 = int(m.group(2))-1
    policy_char = m.group(3)
    password = m.group(4)
    return (password[pos1] == policy_char) ^ (password[pos2] == policy_char)

assert len(list(filter(validate_1,policy_password_list))) == 2
assert len(list(filter(validate_1,policy_password_list))) == 2
with open("./input.txt") as f:
    input = f.readlines()
print(len(list(filter(validate_2,input))))