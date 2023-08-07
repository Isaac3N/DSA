# loop sum
def loop_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(loop_sum([1, 2, 3, 4]))


# for recursive sum, check if the list is empty
# if the list is empty return 0
# else return index element 0 plus the sum of the remaining elements in the list

def recursive_sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print("recursive sum", recursive_sum([1, 2, 3, 4]))
