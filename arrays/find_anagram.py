

def find_anagram(s, p):
    size = len(p)
    sorted_p = sorted(p)   
    word_index = []
    l = 0
    for r in range(size, len(s)+1):
        print(r)
        sorted_seg = sorted(s[l:r])
        print(s[l:r])
        if sorted_seg == sorted_p: 
             word_index.append(l)
        l+=1

    return word_index


# def find_anagram(s,p): 
#     if len(p) > len(s): return []

#     for i in range 





s, p = "abab", "ab"

print(find_anagram(s,p))