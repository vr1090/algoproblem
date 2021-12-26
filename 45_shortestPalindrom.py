# Parameters:
#  str: str
# return type: str

def shortestPalindrome(str):
    # hmm .. cari dulu
    minLongest =0
    for i in range(len(str)+1):
        if str[:i] == str[:i][::-1]:
            minLongest = i

    return str[minLongest:][::-1]+ str
    # titik terakhir palindrom
    # abis itu substring yg position
    # terus hit