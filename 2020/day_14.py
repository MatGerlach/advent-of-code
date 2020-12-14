import re
mask_regex=r'^mask\s+=\s+([X10]+)$'
mem_regex=r'^mem\[(\d+)\]\s+=\s+(\d+)$'
test_input_1="""mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
test_input_2="""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

def apply_mask_1(number,mask):
    number = format(number,'036b')
    masked_as_string ="".join(map(lambda m,n: n if m=="X" else m ,mask,number))
    return int(masked_as_string,2)

def parse_code_1(text):
    lines = iter(text.splitlines())
    memory = {}
    mask=""
    while True:
        line = next(lines,None)
        if line is None:
            break
        if re.match(mem_regex,line) is not None:
            r=re.match(mem_regex, line)
            mem_address=int(r.group(1))
            mem_value=apply_mask_1(int(r.group(2)),mask)
            memory[mem_address] = mem_value
        else:
            mask = re.match(mask_regex,line).group(1)
    return sum(memory.values())
assert parse_code_1(test_input_1) == 165

def apply_mask_2(number,mask):
    number = format(number,'036b')
    masked_as_string ="".join(map(lambda m,n: n if m=="0" else m ,mask,number))
    xs=masked_as_string.count("X")
    masked_number=masked_as_string.replace("X","{}")
    numbers=[]
    for i in range(0,2**xs):
        fill_in = format(i,'0'+str(xs)+'b')
        numbers.append(int(masked_number.format(*fill_in),2))
    return numbers

def parse_code_2(text):
    lines = iter(text.splitlines())
    memory = {}
    mask=""
    while True:
        line = next(lines,None)
        if line is None:
            break
        if re.match(mem_regex,line) is not None:
            r=re.match(mem_regex, line)
            mem_addresses=apply_mask_2(int(r.group(1)),mask)
            mem_value=int(r.group(2))
            for mem_address in mem_addresses:
                memory[mem_address] = mem_value
        else:
            mask = re.match(mask_regex,line).group(1)
    return sum(memory.values())
assert parse_code_2(test_input_2) == 208

with open("input_day_14.txt") as f:
    text= f.read()
print(parse_code_1(text))
print(parse_code_2(text))