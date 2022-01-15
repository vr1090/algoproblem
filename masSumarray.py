def maxSubarray(arr, k):
    sumFirstK = sum( arr[i] for i in range(k) )
    maxSubArray = sumFirstK

    for i in range(len(arr)-k):
        sumFirstK = sumFirstK - arr[i] + arr[i+k]
        maxSubArray = max( maxSubArray, sumFirstK)
    
    return maxSubArray


if __name__ == "__main__":
    array = [5,-10,90,100]
    result = maxSubarray(array, 2)
    print("result berapa..",result)
    assert( result == 190)