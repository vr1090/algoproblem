# Parameters:
#  arr: List[int]
# return type: List[List[int]]

def getPermutations(arr):
    result=[]
    if(len(arr) == 1):
        return [ arr[:] ]
    else:
        for i in range( len(arr)):
            n = arr.pop(0)
            subPermutation = getPermutations(arr)
            for resSub in subPermutation:
                resSub.append(n)
                result.append(resSub)

            arr.append(n)
    return result

def main():
    cupu = [1,2,3]
    result = getPermutations(cupu)
    assert( 6 == len(result))
    

if __name__=="__main__":
    main()