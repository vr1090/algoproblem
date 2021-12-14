def minArrayRotated(arr):
    left = 0
    right = len(arr)-1

    #check if it is a right condition
    # means that there is no rotatted array

    if( arr[left]) < arr[right]: 
        return arr[left]

    while left < right:
        mid = (left + right) // 2

        if (arr[mid] < arr[mid-1]):
            return arr[mid]
        if arr[mid+1] < arr[mid]:
            return arr[mid+1]
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right =mid -1
    
    return arr[left]

def main():
    assert(minArrayRotated([4,5,6,7,8,1,2,3,4]) == 1)
    assert( minArrayRotated([4,5,1,2,3])== 1)

if __name__=="__main__":
    main()


