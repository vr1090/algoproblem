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

def main():
    assert(4 == lcs("abcd","abcd"))

if __name__=="__main__":
    main()