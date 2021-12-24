logging = True

def log(*data):
    if logging :
        print(data)


def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)

    dpTable = [ [0] * (m+1) for i in range(n+1)]
    

    for i in range(1, n+1): dpTable[i][0] = i
    for j in range(1, m+1): dpTable[0][j] = j

    

    for i in range (1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dpTable[i][j] = dpTable[i-1][j-1]
            else:
                dpTable[i][j] = 1+ min( dpTable[i-1][j], dpTable[i][j-1], dpTable[i-1][j-1])



    return dpTable[n][m]

def main():
    assert(0==minDistance("",""))
    assert(1 == minDistance("abc","abd"))

if __name__ == "__main__":
    main()

    
