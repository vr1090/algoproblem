def nQueens(n):
    board = [[0]* n for i in range(n)]
    return _n_queens(n, board, 0)

def _n_queens(n, board, row):
    if n == row:
        return 1
    
    sum = 0

    for col in range(n):
        if isNotAttacked(board,col, row):
            board[row][col]="Q"
            sum += _n_queens(n, board, row+1)
            board[row][col]=""
    return sum

def isNotAttacked(board, col, row):
    i = row -1
    leftWing = col -1
    rightWing = col + 1

    #mundur terus bang
    while i >= 0 :
        if board[i][col] == "Q":
            return False
        elif leftWing >=0 and board[i][leftWing] == "Q":
            return False
        elif rightWing < len(board) and board[i][rightWing] == "Q":
            return False
        else:
            i -= 1
            leftWing -= 1
            rightWing += 1
    return True


def main():
    result = nQueens(4)
    print(result)
    assert(2 == result)


if __name__ == "__main__":
    main()