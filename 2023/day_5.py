import utils


class Map:
    def __init__(self, input):
        rules = {}
        rules[0] = 0
        for line in input:
            dst_start, src_start, length = map(int, line.split())
            rules[src_start] = dst_start-src_start
            if not src_start+length in rules:
                rules[src_start+length] = 0
        self._rules = dict(
            sorted(rules.items(), key=lambda x: x[0], reverse=True))

    def translate(self, number):
        """
        >>> Map(["50 98 2","52 50 48"]).translate(51)
        53
        >>> Map(["50 98 2","52 50 48"]).translate(1)
        1
        >>> Map(["50 98 2","52 50 48"]).translate(98)
        50
        >>> Map(["50 98 2","52 50 48"]).translate(1000)
        1000
        """
        for start, rule in self._rules.items():
            if number >= start:
                return number + rule

    def combine(self, other):
        """
        >>> Map(["50 98 2","52 50 48"]).combine(Map(["0 15 37","37 52 2","39 0 15"])).translate(98)
        35
        """
    	for start,rule in self._rules.items()
            
def task_1(input):
    seeds = map(int, input[0].split()[1:])
    maps = {}
    name = ""
    for line in input[2:]:
        if line == "":
            continue
        if utils.is_digit(line[0]):
            maps[name].append(line)
        else:
            name = line.split()[0]
            maps[name] = []
    mapper = {}
    for name, m in maps.items():
        mapper[name] = Map(m)

    locations = []
    for seed in seeds:
        soil = mapper["seed-to-soil"].translate(seed)
        fertilizer = mapper["soil-to-fertilizer"].translate(soil)
        water = mapper["fertilizer-to-water"].translate(fertilizer)
        light = mapper["water-to-light"].translate(water)
        temperature = mapper["light-to-temperature"].translate(light)
        humidity = mapper["temperature-to-humidity"].translate(temperature)
        location = mapper["humidity-to-location"].translate(humidity)
        locations.append(location)
    return (min(locations))


def task_2(input):
    seeds = map(int, input[0].split()[1:])
    maps = {}
    name = ""
    for line in input[2:]:
        if line == "":
            continue
        if utils.is_digit(line[0]):
            maps[name].append(line)
        else:
            name = line.split()[0]
            maps[name] = []
    mapper = {}
    for name, m in maps.items():
        mapper[name] = Map(m)

    locations = []
    for seed in seeds:
        soil = mapper["seed-to-soil"].translate(seed)
        fertilizer = mapper["soil-to-fertilizer"].translate(soil)
        water = mapper["fertilizer-to-water"].translate(fertilizer)
        light = mapper["water-to-light"].translate(water)
        temperature = mapper["light-to-temperature"].translate(light)
        humidity = mapper["temperature-to-humidity"].translate(temperature)
        location = mapper["humidity-to-location"].translate(humidity)
        locations.append(location)
    return (min(locations))


if __name__ == "__main__":
    input = utils.load_input(5)
    print("Solution 1:")
    print(task_1(input))
    print("Solution 2:")
    # print(task_2(input))
