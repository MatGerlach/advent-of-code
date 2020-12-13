def get_seat_nr(code):
    """Transform a code into a seat nr
    See https://adventofcode.com/2020/day/5

    >>> get_seat_nr("BFFFBBFRRR")
    567
    >>> get_seat_nr("FFFBBBFRRR")
    119
    >>> get_seat_nr("BBFFBBFRLL")
    820
    """
    row=int(code[:7].replace("F","0").replace("B","1"),2)
    column=int(code[7:].replace("L","0").replace("R","1"),2)
    seat=row*8+column
    return seat

def get_seat_nrs(codes):
    """Transform a list of codes into a list of seat nrs
    See https://adventofcode.com/2020/day/5

    >>> get_seat_nrs(["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"])
    [567, 119, 820]
    """
    return list(map(lambda code: get_seat_nr(code),codes))

def get_max_seat_nr(codes):
    """Get the highest seat nr in use
    See https://adventofcode.com/2020/day/5
    
    >>> get_max_seat_nr(["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"])
    820
    """
    return max(get_seat_nrs(codes))

def get_free_seats(codes):
    """Get the set of free seat numbers
    See https://adventofcode.com/2020/day/5
    
    >>> get_free_seats(["BFFFBBFRLL","BFFFBBFRRL","BFFFBBFRRR"])
    {565}
    """
    codes = sorted(get_seat_nrs(codes))
    available_codes = range(codes[0],codes[-1]+1)
    return set(codes).symmetric_difference(set(available_codes))

def get_results():
    with open("input_day_5.txt") as f:
        codes = f.read().splitlines()
    print("The highest seat number is {highest}.".format(highest=get_max_seat_nr(codes)))
    print("The only free seat number is {free}.".format(free=get_free_seats(codes).pop()))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    get_results()

    