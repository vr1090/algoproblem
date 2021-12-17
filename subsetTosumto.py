def subsetsThatSumUpToK(arr, k, i=0, sum=0):
    if i== len(arr) and sum == k:
        return 1
    elif i==len(arr):
        return 0
    else:
        result = subsetsThatSumUpToK(arr,k, i+1, sum+ arr[i]) \
            + subsetsThatSumUpToK(arr,k, i+1,sum )
        return result
  

def main():
    result = subsetsThatSumUpToK([1,2,3,1],4)
    print(result)
    assert( result == 3)

if __name__ == "__main__":
    main()