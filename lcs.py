def lcs(str1, str2,i=0,j=0, memoization={}):
    key = str(i) +" "+str(j)

    if memoization.get(key) is not None:
        return memoization[key]

    if i == len(str1) or j == len(str2):
        return 0
    elif str1[i] == str2[j]:
        return 1 + lcs(str1, str2, i+1, j+1)
    else:
        result = max( lcs(str1, str2, i+1, j), lcs(str1, str2, i,j+1))
        memoization[key] = result
    
    return memoization[key]


def lcs2(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [ [0] * (m+1) for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max( dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]


def main():
    assert(4 == lcs("abcd","abcd"))
    assert(2 == lcs("abgcdadga", "cdff"))
    assert(4 == lcs2("abcd","abcd"))
    assert(2 == lcs2("abgcdadga", "cdff"))


if __name__=="__main__":
    main()