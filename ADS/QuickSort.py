import random


def split(a: list, x: int) -> tuple:
    less = []
    equal = []
    more = []

    for e in a:
        if e < x:
            less.append(e)
        elif e == x:
            equal.append(e)
        else:
            more.append(e)

    return less, equal, more


def sort(a: list) -> list:
    if len(a) <= 1:
        return a
    else:
        x = random.choice(a)
        s = split(a, x)

        return sort(s[0]) + s[1] + sort(s[2])


a = [3, 6, 4, 8, 7, 5, 1, 2, 9, 0]
print(sort(a))

