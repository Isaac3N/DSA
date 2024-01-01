# binary search example

def binary_search(list, item):
    # low and high keep track of which part of the you'll search in
    low = 0
    high = len(list) - 1

    # while you have not narrowed it down to one element ..

    while low <= high:
        # ... check the middle element
        mid = (low+high)//2
        # mid_int = int(mid)
        guess = list[mid]
        # found the item
        if guess == item:
            return mid

            # the guess was too high

        if guess > item:
            high = mid - 1

            # if guess was too low
        else:
            low = mid + 1

            # Item does not exist
    return []


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
