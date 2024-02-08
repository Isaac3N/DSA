def min_max(array):
    n = len(array)

    l = 0
    max_value = -10000000000

    for r in range(n):
        max_value = max(array[r], max_value)

        if array[l] > array[r]:
            l = r 

    return(array[l], max_value)


array = [4,2, 0, 8, 20, 9, 2]

print(min_max(array))