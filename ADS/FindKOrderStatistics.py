import random


def split(a: list, l: int, r: int) -> int:
    x = random.choice(a)

    m = l
    
    for i in range(l, r):
        if a[i] < x:
            a[i], a[m] = a[m], a[i]
            m += 1
    return m


def find(a: list, k: int) -> int:
    l = 0
    r = len(a)

    while True:
        m = split(a, l, r)

        if m == k:
            return a[m]
        elif k < m:
            r = m
        else:
            l = m + 1


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find(a, 4))

