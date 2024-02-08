def rotate_image(image):
    n = len(image)
    rotated_image = [[-1]*n for _ in range(n)]

    for i in range(n):
        print(image[i])
        for j in range(n):
            print(image[i][j])
            rotated_image[n-j-1][i] = image[i][j]

    return rotated_image



image = [[1,2,3], [4,5,6], [7,8,9]]

print(rotate_image(image))

