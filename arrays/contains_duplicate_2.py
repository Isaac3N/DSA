from collections import defaultdict

# def contains_duplicate2(nums, k):
#     hashmap = defaultdict(list)
#     n = len(nums)

#     for i in range(n):             
#         hashmap[nums[i]].append(i)

#     for v in hashmap.values():
#         print(v)
#         if len(v) >= 2:
#             l,r = 0, 1
#             while r<=len(v):
#                 if abs(v[r]- v[l]) <= k: 
#                     return True 
#                 l= r
#                 r+=1 

#     return False 

## more efficient solution using sets -- solution is twice as efficient

def contains_duplicate2(nums, k): 
    hashset = set ()
    n = len(nums)
    l = 0

    for r in range(n): 
        if r-l >k:
            hashset.remove(nums[l])
            l+=1 
        if nums[r] in hashset: 
            return True 

        else: 
            hashset.add(nums[r])

    return False


        

nums = [1,0,1,1]
print(contains_duplicate2(nums, 2))