import re

rule_regex = r'^(.+)s contain (.+)\.$'


def parse_rules(text):
    rules = {}
    for line in text:
        m = re.match(rule_regex, line)
        if m.group(2) == "no other bags":
            rule = []
        else:
            rule = list(
                map(lambda x: tuple(x.rstrip("s").split(" ", 1)), m.group(2).split(", ")))
        rules[m.group(1)] = rule
    return rules


def get_all_sub_bags(bag, rules):
    rule = rules[bag]
    if len(rule) == 0:
        return [bag]
    else:
        sub_bags = [bag]
        for (_, sub_bag) in rule:
            sub_bags += get_all_sub_bags(sub_bag, rules)
        return sub_bags


def get_number_of_bags(bag, rules):
    rule = rules[bag]
    if len(rule) == 0:
        return 1
    else:
        nr_sub_bags = 1
        for (count, sub_bag) in rule:
            nr_sub_bags += int(count) * get_number_of_bags(sub_bag, rules)
        return nr_sub_bags


def get_all_bag_combinations(rules):
    combination = []
    for (bag, _) in rules.items():
        combination.append(get_all_sub_bags(bag, rules))
    return combination


with open('input_day_7.txt') as f:
    content = f.read().splitlines()

rules = parse_rules(content)
combinations = get_all_bag_combinations(rules)
shiny_combinations = list(
    filter(lambda c: "shiny gold bag" in c, combinations))
print("Number of combinations containing atleast one shiny gold bag: {}"
      .format(len(shiny_combinations)-1))
print("Number of bags in one shiny gold bag: {}"
      .format(get_number_of_bags("shiny gold bag", rules)-1))
