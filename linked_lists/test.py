def searchMatrix(matrix, target):

    n_col = len(matrix)
    n_row = len(matrix[0])
    top = 0
    bottom = n_col-1


    # if n_col-1 == 0:
        

    while top <= bottom: 
        mid_col = (top+bottom)//2


        if target > matrix[mid_col][0] and target > matrix[mid_col][n_row-1]:
            top = mid_col + 1 

        elif target < matrix[mid_col][0] and target < matrix[mid_col][n_row-1]:
            bottom = mid_col - 1

        elif target >= matrix[mid_col][0] and target <= matrix[mid_col][n_row-1]: 
            l, r = 0, n_row-1
          
            while l <= r: 
                mid_row = (l+r)//2

                if target > matrix[mid_col][mid_row]: 
                    l = mid_row + 1 

                elif  target<matrix[mid_col][mid_row] :
                    r = mid_row -1 
                   

                else: 
                    return True 
            return False 

    return False 


matrix = [[1,3]]

target = 3

print(searchMatrix(matrix, target))
