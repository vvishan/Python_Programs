def Rotate_Image(matrix):
    n = len(matrix)
    # now we just transpose the matrix
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    # now we can get the roatated image by using the reflection

    for i in range(n):
        for j in range(n //2):
            matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
    return matrix

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(Rotate_Image(mat))