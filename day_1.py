original=[1721,979,366,299,675,1456]
target=2020
result_1_1=514579
result_1_2=241861950

def recursive(candidates, target):
    if len(candidates)==0:
        return set()
    matches = set()
    for candidate in candidates:
        rest   = target - candidate
        if rest in candidates:
            matches.add(frozenset([candidate, rest]))
        else:
            results = recursive(filter(lambda x: x < rest and x != candidate,candidates) , rest)
            if len(results) > 0:
                for result in results:
                    matches.add(frozenset(result.union(set({candidate}))))
    return matches

def oneline_1_1(o,t):
    return (lambda x:x[0]*x[1])(list(set(map(lambda x:t-x,o)) & set(o)))

def oneline_1_1_but_readable(o,t):
    return [x*y for x in o for y in o if x+y==t]

def oneline_1_2(o,t):
    return (lambda x:(t-x[0])*(t-x[1])*(t-x[2]))(list(set(map(lambda x:t-x,o)) & set([x+y for x in o for y in o])))

def oneline_1_2_but_readable(o,t):
    return [x*y*z for x in o for y in o for z in o if x+y+z==t]

assert oneline_1_1(original,target) == result_1_1
assert result_1_1 in oneline_1_1_but_readable(original,target)
assert oneline_1_2(original,target) == result_1_2
assert result_1_2 in oneline_1_2_but_readable(original,target)

result_final=[]
for result in recursive(original,target):
    product = 1
    for x in result:
        product *= x
    result_final.append(product)
assert result_1_1 in result_final
assert result_1_2 in result_final