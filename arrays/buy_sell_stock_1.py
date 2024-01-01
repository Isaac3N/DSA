def buy_sell_stock(nums):
    n = len(nums)
    l,r = 0, 1

    largest_profit = 0

    while r< n: 
        difference = nums[r] - nums[l] 
        if difference > largest_profit:  
            largest_profit = difference 
            r+=1 
        elif difference<0: 
            l = r 
            r+=1 
        else: 
            r+=1
    return largest_profit

nums = [310,315,275,295,260,270,290,230,255,250]

print(buy_sell_stock(nums))
