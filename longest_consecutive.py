from collections import defaultdict

def longest_consecutive(nums): 
    map = defaultdict(int)
    n = len(nums)

    for i in range(n): 

        map[nums[i]] = 1

        if nums[i] + 1 in map: 
            map[nums[i]] += map[nums[i]+1]
            map[nums[i]+1] = map[nums[i]]


        if nums[i] - 1 in map: 
            map[nums[i]] += map[nums[i]-1]
            map[nums[i]-1] = map[nums[i]]

    print(map)


nums = [0,3,7,2,5,8,4,6,0,1]

longest_consecutive(nums)
