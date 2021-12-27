# Parameters:
#  board: List[List[char]]
#  word: str
# return type: bool

def exist(board, word):
    n = len(board)
    m = len(board[0])
    visited = set()
    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                if search(board, word, i,j,0,visited ):
                    return True
    
    return False


def outofboard(board, i,j):
    n = len(board)
    m = len(board[0])

    return i < 0 or i >= n or j < 0 or j >=m

def search(board, word, i, j, count, visited):
    if count == len(word):
        return True
    
    if  outofboard(board, i,j) or (i,j) in visited or board[i][j] != word[count] :
        return False

    visited.add((i,j))
    if search(board, word, i+1,j, count+1, visited) or \
       search(board, word,i-1, j, count+1, visited) or \
       search(board, word,i, j+1, count+1, visited) or \
       search(board, word, i, j-1, count+1, visited):
           return True
    else:
         visited.remove( (i,j))
    return False


    