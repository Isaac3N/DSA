# def contains_duplicate(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] == nums[j]:
#                 return True

#             return False


# # Example usage:
# nums = [1, 2, 3, 1]
# result = contains_duplicate(nums)
# print(result)  # Output: True


# def selection_sort(nums):
#     n = len(nums)
#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]

#     return nums


# def contains_duplicate(nums):
#     selection_sort(nums)
#     for i in range(0, len(nums)-1):
#         if nums[i] == nums[i + 1]:
#             return True
#     return False


# # Example usage:
# nums = [1, 2, 3, 1, 7, 3, 8, 5, 3]
# print(contains_duplicate(nums))
# result = contains_duplicate(nums)
# print(result)  # Output: True


# def selection_sort(nums):
#     n = len(nums)

#     for i in range(n-1):
#         min_index = i

#         for j in range(i+1, n):
#             if nums[min_index] > nums[j]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]

#     return nums


# def contains_duplicate(nums):
#     selection_sort(nums)
#     n = len(nums)

#     for i in range(0, n):
#         if nums[i] == nums[i+1]:
#             return True

#     return False


# nums = [5, 1, 4, 2, 7, 3, 3]

# print(selection_sort(nums))


# print(contains_duplicate(nums))


# def qsort(nums):
#     if len(nums) < 2:
#         return nums

#     else:
#         pivot = nums[0]
#         less = [i for i in nums[1:] if i <= pivot]

#         greater = [i for i in nums[1:] if i > pivot]

#         return qsort(less) + [pivot] + qsort(greater)


# def contains_duplicate(nums):
#     qsort(nums)

#     for i in range(len(nums)):
#         if nums[i] == nums[i+1]:
#             return True

#         return False


# nums = [1, 2, 3, 1]
# result = qsort(nums)
# print(result)


def contains_duplicates(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


nums = [1, 2, 3, 1]
result = contains_duplicates(nums)
print(result)
