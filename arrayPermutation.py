# Parameters:
#  arr: List[int]
# return type: List[List[int]]

def getPermutations(arr):
    result=[]
    print("get permutation",arr)
    if(len(arr) <= 1):
        return [ arr[:] ]
    else:
        for i in range( len(arr)):
            n = arr.pop(0)
            subPermutation = getPermutations(arr)
            print("sub ermutation", subPermutation, "yg di pop",n)
            for resSub in subPermutation:
                resSub.append(n)
                if resSub not in result:
                    result.append(resSub)

            arr.append(n)
    print("result",result)
    return result

def main():
    cupu = [1,2,3]
    result = getPermutations(cupu)
    assert( 6 == len(result))
    result = getPermutations([])
    assert( 1 == len(result))
    

if __name__=="__main__":
    main()