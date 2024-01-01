# def minimum_sub_array(array, num):

#     l, r = 0, 0
#     result = []

#     sum = array[l]

#     while r > len(array):

#         if sum == num:
#             result.append(sum)
#             l += 1
#             r = l

#         elif sum < num:
#             r += 1
#             sum += array[r]

#         elif sum > num:
#             sum = 0
#             l += 1
#             r = l

#     length_res = len(result)

#     return length_res


l, r = 0, 0
nums = [1, 4, 4]
result = []
target = 4
sum = nums[l]


while r < len(nums):
    if sum == target:
        result.append([nums[l:r+1]])
        l += 1
        r = l
        if r < len(nums):
            sum = nums[l]
    elif sum < target:
        r += 1
        if r < len(nums):
            sum += nums[r]
    else:
        sum -= nums[l]
        l += 1


print(result)


# while r < len(array):

#     if sum == num:
#         result.append(sum)
#         print("hey", result)
#         l += 1
#         r = l

#     elif sum < num:
#         r += 1
#         print(array[r])
#         sum += array[r]

#     elif sum > num:
#         sum = 0
#         l += 1
#         r = l

# print(length_res)


# print(minimum_sub_array([7, 3, 1, 2, 4, 3], 7))
