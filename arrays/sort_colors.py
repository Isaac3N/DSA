#sort colors using bucket sort, a two pass solution


def sort_colors(nums):
    num_map ={0: 0, 1:0, 2:0}

    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1 

    print(num_map)
    count = 0 
    for key, value in num_map.items():
        print(key, value)
        for j in range(value): 
            print(num_map[j])
            nums[count] = key
            count += 1
    

    print(nums)

nums = [2,0,2,1,1, 2]
sort_colors(nums)
            