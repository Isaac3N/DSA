
def reverse_string(string):
    
    string_array = string.split(" ")

    for i in reversed(string_array):
        print(i, end=" ")



string = "Bob likes Alice"

reverse_string(string)

