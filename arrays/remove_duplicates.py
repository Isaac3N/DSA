
def remove_dupes(nums):
    l = 1
    n = len(nums)

    for r in range(1, n):
        if nums[r] != nums[r-1]: 
            nums[l] = nums[r]
            l+=1 
    return l
       



nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(remove_dupes(nums))

    
    