# advancing through an array by shifting the goal post each time using greedy algorithm

def jump_game(nums): 
    goal = len(nums) -1 
    n = len(nums)
    
    for i in range(n-1, -1, -1):
        if i+ nums[i] >= goal:
            goal = i 

    return True if goal == 0 else False 



nums = [3,1,1,0,2,1,1]


print(jump_game(nums))