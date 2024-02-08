

from math import inf

def substring(array):
    n = len(array)
    l, r = 0, 0

    hashmap = {}

    max_substring = float(-inf)

    while  r < n:
        if array[r] in hashmap: 
            l = hashmap[array[r]] + 1
            del hashmap[array[r]]


        else: 
            hashmap[array[r]] = r
            max_substring = max(max_substring, (r-l+1))
            r += 1 

    print(len(hashmap))

    return max_substring



array = "abba"





print(substring(array))
            
