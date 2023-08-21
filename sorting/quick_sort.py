# code sample for quick sort

def qsort(array):
    if len(array) < 2:
        # returning the array because base case of elements 0 to 1 are already sorted
        return array

    else:
        # recursive case
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]

        return qsort(less) + [pivot] + qsort(greater)


print(qsort([10, 5, 2, 3, 7, 11, 23]))
