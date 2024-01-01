

def q_sort(nums):
    l, i, r =  0, 0, len(nums)-1

    while i <= r: 
        if nums[i] == 0: 
            nums[i], nums[l] = nums[l], nums[i]
            l+=1 
            i+=1 

        elif nums[i] == 1: 
            i+=1 
        else: 
            nums[i], nums[r] = nums[r], nums[i] 
            r-=1 

    
    return nums 


nums = [0,2, 1, 0, 2, 1]

print(q_sort(nums))

