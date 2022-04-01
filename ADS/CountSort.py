def sort(a: list) -> list:
    counter = [0 for _ in range(max(a) + 1)]

    for e in a:
        counter[e] += 1
    
    a = []
    for i, count in enumerate(counter):
        a += [i] * count
    
    return a


a = [3, 2, 1, 5, 4, 6, 9, 0, 7, 8]
print(sort(a))

