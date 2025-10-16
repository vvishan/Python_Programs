arr = [1,2,3,4]
# n= len(arr)
# result = [0]*n
# print(result)
s = "VIX"
d = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':150}

st =["flow","flower","float"]
i =0
print(s[:1])

#print(3//2)
matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate_image(matrix):

    n = len(matrix)

    # transpose

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    print(matrix)
    # reflection
    for i in range(n):
        for j in range(n //2):
            matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
            print(matrix)
    


rotate_image(matrix)    