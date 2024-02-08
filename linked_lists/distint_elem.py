

def distinct_elements(array):
    hashset = set()

    for i in array: 
        hashset.add(i)


    return len(hashset)


array = [1, 1, 1, 3, 4, 2, 3]

print(distinct_elements(array))