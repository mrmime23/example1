def oneFunction(a):
    aNumber = 0
    p = None

    for v in a:
        if p is None or v > p:
            aNumber += v
            p = v
        elif v < p:
            aNumber = 0
            p = None

    return aNumber


#assert f1([]) == 0
assert oneFunction([0]) == 0
assert oneFunction([1]) == 1
assert oneFunction([1, 2, 3]) == 6
assert oneFunction([-1, 1]) == 0
assert oneFunction([1, 2, 3, 4]) == 10
assert oneFunction([1, 2, 3, -4]) == 0
assert oneFunction([-1]) == -1
assert oneFunction([1, 2, 3, 3]) == 6
assert oneFunction([3, 3, 3, 3, 3]) == 3
assert oneFunction([-1, -2, -3]) == -3
assert oneFunction([1000000]) == 1000000
assert oneFunction([1, 2, 3, 4, 1]) == 0
assert oneFunction([1, 2, 3, 4, 1, 2]) == 2
assert oneFunction([1, 3, 5, 42, 1])
#assert f1([1, 2, 3, 3, 4, 1, 2, 3]) == 5
