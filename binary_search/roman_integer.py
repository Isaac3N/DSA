def roman_integer(strings): 

    n = len(strings)
    ri_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    conversion = [ri_map[strings[0]]]


    for i in range(1, n): 
        if ri_map[strings[i]] > conversion[-1]: 
            new_digit = ri_map[strings[i]] - conversion[-1]
            conversion.pop()
            conversion.append(new_digit)

        else: 
            conversion.append(ri_map[strings[i]])

    return sum(conversion)


strings = "MCMXCIV"

print(roman_integer(strings))