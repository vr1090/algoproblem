# Parameters:
#  str: str
# return type: List[str]

def getSubsequences(str):
    # your code here
    result = []

    def recSubsequence(str, length, sequence):
        if length == len(str):
            result.append(sequence)
        else:
            recSubsequence(str, length+1, sequence+ str[length])
            recSubsequence(str, length+1, sequence)
    
    recSubsequence(str, 0, "")
    return result

if __name__=="__main__":
    print(getSubsequences("abc"))