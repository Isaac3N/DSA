
def leaders_array(nums):
    n = len(nums)

    leaders = [nums[0]]

    # for i in range(1,n):
    #     while leaders and nums[i] > leaders[-1]:
    #         leaders.remove(leaders[-1])

    #     leaders.append(nums[i])

    # return leaders 

    

nums = [1,2,3,4,5,6]

print(leaders_array(nums))


