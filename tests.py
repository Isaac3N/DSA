# my_dict = {'apple': 5, 'banana': 2, 'orange': 5, 'grape': 3}


# print(sorted(my_dict.items()))
# # sorted_items = sorted(my_dict.items(), key=lambda x: (x[1], x[0]))

# # sorted_dict = dict(sorted_items)

# print(sorted_items)

def product(nums):
    n = len(nums)

    total = nums[0] 

    for i in range(1, n):  
        total *= nums[i]

    for i in range(0,n):
        if nums[i] == 0: 
            nums = [[0]*(n-1)]

        else:
            nums[i] = total//nums[i]

    return nums


nums = [1,2,3,0,4,5]
print(product(nums))
