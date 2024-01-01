def increment_nums(nums):
    n=len(nums) + 1
    r = len(nums)-1 
    l = 0

    if nums[r] <9:
        nums[r] += 1
        return nums 

    while nums[r] +1 > 9: 
        print(nums[r])
        if nums[r-1] < 9:
            nums[r] = 0
            nums[r-1] += 1
            print("here")
            return nums 
             

        elif nums[r-1] == nums[l] and r<=1 :
            nums[r] = 0
            nums.append(0)
            nums[l] = 1
            return nums
        
        else: 
            nums[r] = 0
            r-=1 




    

nums = [9, 8, 9, 9]
print(increment_nums(nums))