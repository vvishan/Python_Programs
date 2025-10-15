m = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]


def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    res =[]
    top , bottom =0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    while left <= right and top <= bottom:
        #left to right on top row
        for i in range(left,right+1):
            res.append(matrix[top][i])
        top += 1
        #top to bottom corner
        for i in range(top,bottom+1):
            res.append(matrix[i][right])
        right -= 1
        #right to left on bottom row
        if left <= right:
             for j in range(right , left-1,-1):
                 res.append(matrix[bottom][j])
             bottom -=1
        # bottom to top approach
        if top <= bottom:
             for j in range(bottom, top -1,-1):
                 res.append(matrix[j][left])
             left +=1
    return res       
        


def practice(mat):
    res=[]

    top,bottom = 0,len(mat)-1
    left, right =0,len(mat[0])-1

    
    for i in range(right, left-1,-1):
        res.append(mat[i][bottom])
    print(res)

print(spiral_matrix(m))
