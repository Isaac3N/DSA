from collections import defaultdict

def group_anagram(strs): 
    res_map = defaultdict(list)
    for word in strs: 
        unicode_rep = [0] * 26
        for char in word: 
            unicode_rep[ord(char)-ord("a")] +=1 

        res_map[tuple(unicode_rep)].append(word)

    return res_map.values()





strs =["ett","tte","tan","ate","nat","bat"]

print(group_anagram(strs))

