from collections import defaultdict

def remove_anagrams(words): 
    hashmap = defaultdict(list)
    new_words = []

    for char in words: 
        sorted_char = tuple(sorted(char))
 
        hashmap[sorted_char].append(char)



    for value in hashmap.values(): 
        new_words.append(value[0])
    return new_words





words = ["a","b","c","d","e"]

print(remove_anagrams(words))