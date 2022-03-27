def merge(a: list, b: list) -> list:
    i = 0
    j = 0

    c = [0 for _ in range(len(a) + len(b))]

    while i < len(a) or j < len(b):
        if j == len(b) or i < len(a) and a[i] < b[j]:
            c[i + j] = a[i]
            i += 1
        else:
            c[i + j] = b[j]
            j += 1
    
    return c


def sort(a: list) -> list:
    n = len(a)
    if n <= 1:
        return a

    l = a[:n//2]
    r = a[n//2:]

    l = sort(l)
    r = sort(r)

    return merge(l, r)


a = [1, 4, 5, 7, 2, 3, 6]

print(sort(a))

