def nQueens(n):
    board = [[0]* n for i in range(n)]
    return _n_queens(n, board, 0)

def _n_queens(n, board, row):
    if n == row:
        return 1
    
    sum =0

    for i in range(n):
        if isNotAttacked(board, i,row):
            board[row][i] = "Q"
            sum += _n_queens(n, board, row+1)
            board[row][i]="."
    return sum

def isNotAttacked(board, col, row):
    left =col -1
    right = col + 1
    i = row -1

    while i >= 0 :
        if board[i][col] == "Q" or (left >=0 and board[i][left] == "Q") or (right < len(board) and board[i][right]=="Q"):
            return False
        else:
            i = i-1
            left = left -1
            right = right +1
    
    return True

def main():
    result = nQueens(4)
    print(result)
    assert(2 == result)


if __name__ == "__main__":
    main()