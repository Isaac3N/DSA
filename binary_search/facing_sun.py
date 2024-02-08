def facing_sun(height):
    n = len(height)
    l = 0
    count = 1
    for r in range(1,n):
        if height[r] > height[l]: 
            count += 1
            l = r 

    return count

height = [7, 4, 10, 8, 11]

print(facing_sun(height))
