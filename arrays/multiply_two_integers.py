def multiply_integers(num1, num2):
    total_sum = 0 
    total_count = 0
    for i in reversed(num2): 
        current_sum = 0 
        current_count = 0

        for r in reversed(num1):      
            product = (r* i) * (10**current_count)
            current_sum += product 

            current_count += 1
        total_sum = total_sum + (current_sum *(10**total_count))

        total_count += 1
    
    return total_sum


print(multiply_integers([6,4], [5,1,1]))
