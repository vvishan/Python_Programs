
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    ["5",".",".",".",".",".",".","6","."],  # duplicate '5' in same column
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"]]
def Isvalidsudoku(board):
    # validate rows
    for i in range(9):
        s= set()
        for j in range(9):
            item = board[i][j]
            if item == '.':
                continue
            if item in s:
                return False
            s.add(item)
    
    #validate cols
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[j][i]
            if item =='.':
                continue
            if item in s:
                return False
            s.add(item)
    #validate the blocks

    start =[(0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6)]

    for i,j in start:
        s=set()
        for row in range(i,i+3):
            for col in range(j,j+3):
                item = board[row][col]
                if item == '.':
                    continue
                if item in s:
                    return False
                s.add(item)
    return True


print(Isvalidsudoku(board))


### other way to solve 
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]  # box index = (r//3)*3 + (c//3)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            if val in rows[r]:
                return False
            rows[r].add(val)

            if val in cols[c]:
                return False
            cols[c].add(val)

            b = (r // 3) * 3 + (c // 3)
            if val in boxes[b]:
                return False
            boxes[b].add(val)

    return True

print(is_valid_sudoku(board))