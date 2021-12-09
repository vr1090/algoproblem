def getLpsArr(str):
    i = 1
    length = 0
    lpsr = [0] * len(str)

    while i < len(str):
        if str[i] == str[length]:
            length += 1
            lpsr[i] = length
            i+=1
        elif length > 0 :
            length = lpsr[length - 1]
        else:
            length = 0
            lpsr[i] = 0
            i += 1
    return lpsr

def substrIndex(str1, str2):
    i = 0
    j = 0

    m = len(str2)
    n = len(str1)

    if( m == 1 and n == 1):
        if str1 == str2:
            return 0
        else:
            return -1

    lpsr = getLpsArr(str2)
    while i < n and j < m:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        elif j > 0 :
            j = lpsr[j-1]
        else:
            i+= 1

    return i -j


        

