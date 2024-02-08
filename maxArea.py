def maxArea(height):

    l,r  = 0, len(height) - 1

    max_area = 0
    
    while l<r: 
        curr_area = min(height[l], height[r]) * (r-l)
        max_area = max(max_area, curr_area)

        if height[l] > height[r]:
            r-=1 

        else:
            l+=1

    return max_area



height = [1,1]

print(maxArea(height))
# print(len(height[1:7]) +1)