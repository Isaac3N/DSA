


def binary_search(nums, key): 

    low, high = 0, len(nums)-1
    n = len(nums)

    while low <= high: 
        mid = (low+ high)//2

        if key > nums[mid]: 
            low = mid +1

        elif key < nums[mid]: 
            high = mid-1

        else: 
            return True
    return False

nums = [1,3]
key = 3

print(binary_search(nums, key))