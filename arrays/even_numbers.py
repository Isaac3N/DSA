def even_odd(nums): 

    l, r = 0, len(nums)-1 

    while l< r: 
        if nums[l] % 2 == 0: 
            l+= 1

        else:  
            nums[l], nums[r] = nums[r], nums[l]
            r-=1 

    return nums 


nums = [2, 3, 4, 6, 7]

even_odd = even_odd(nums)

print(even_odd)