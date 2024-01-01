#more elegant solution for plus one problem

def plus_one(nums):
    nums[-1] +=1 

    for i in reversed(range(len(nums))):
        if nums[i]!= 10:
            break 
        nums[i-1] +=1
        nums[i] = 0 

    if nums[0] == 10: 
        nums[0] = 1
        nums.append(0)

    return nums


            

nums = [9, 8, 9, 9]
print(plus_one(nums))