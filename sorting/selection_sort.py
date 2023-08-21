# writes a function to sort an array from smallest to largest using selection sort 0(n^2)

# def findSmallest(arr):
#     smallest = arr[0]  # Initialize 'smallest' to the first element of the list
#     # Initialize 'smallest_index' to 0 (index of the first element)
#     smallest_index = 0

#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             # Update 'smallest' to the current element if it is smaller
#             smallest = arr[i]
#             smallest_index = i  # Update 'smallest_index' to the index of the current elements
#     return smallest_index  # Return the index of the smallest element in the list


# # selection sort algorithm

# def selectionSort(arr):
#     newArr = []  # Initialize an empty list 'newArr' to store the sorted elements
#     for i in range(len(arr)):
#         # Find the index of the smallest element in 'arr' using 'findSmallest' function
#         smallest = findSmallest(arr)
#         # Remove the smallest element from 'arr' and append it to 'newArr'
#         newArr.append(arr.pop(smallest))
#     return newArr  # Return the sorted list 'newArr'
# print(findSmallest([5, 3, 6, 10]))

def selectionSort(nums):
    n = len(nums)

    for i in range(n-1):
        min_index = i

        for j in range(i, n-1):
            if nums[min_index] > nums[j]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums


nums = [5, 1, 2, 3, 1]
print(selectionSort(nums))
