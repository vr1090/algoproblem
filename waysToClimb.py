# Parameters:
#  n: int
#  possibleSteps: Set[int]
# return type: int

def waysToClimb(n, possibleSteps):
    possible = []
    def ways(n, count):
        if count >= n:
            possible.append(count)
        else:
            for x in possibleSteps:
                ways(n, count + x)
    
    ways(n,0)

    count = 0
    for c in possible:
        if c == n:
            count += 1
    
    return count

def waysToClimb2(n, possibleStep):
    dpTable = [0] * (n+1)
    dpTable[0] = 1

    for index in range(1, n+1):
        solution = 0
        for step in possibleStep:
            if( index - step) >=0:
                solution += dpTable[index-step]
        dpTable[index] = solution
    return dpTable[n]

def main():
    result = waysToClimb(5,{1,3,4})
    assert( 6 == result)
    result = waysToClimb2(5, {1,3,4})
    print(result)
    assert( 6 == result)

if __name__ == "__main__":
    main()# Parameters:
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
    return False# Parameters:
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
    return Fals# Parameters:
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


    e# Parameters:
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
    return False# Parameters:
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


    


    


    


    