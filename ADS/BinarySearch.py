def binary_search(array: list, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == x:
            return middle
        elif array[middle] < x:
            left = middle + 1
        elif array[middle] > x:
            right = middle - 1

    return -1


a = print(binary_search([1, 2, 3, 4, 7, 9], 7))

