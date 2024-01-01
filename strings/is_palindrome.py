
from curses.ascii import isalnum


def is_palindrome(string):
    

    new_string = ""

    for i in string:  
        if i.isalnum(): 
            new_string += i.lower() 

    l, r = 0, len(new_string)-1

    print("hey", new_string)

    while l< r: 
        if new_string[l] != new_string[r]: 
            return False 
        l+=1 
        r-=1 
    return True 

    


string = "A man, a plan, a canal, Panama."

print(is_palindrome(string))