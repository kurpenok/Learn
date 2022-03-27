def sort(a: list) -> list:
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


a = [5, 6, 7, 8, 1, 2, 0, 3, 4, 5, 9]

print(sort(a))

